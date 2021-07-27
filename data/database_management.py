"""
    This file aims to work over the database. It creates a 'Database' object with it's own methods to getting the
    info we want.
"""
import logging
import string

from data.database_connection import DatabaseConnection as DatabaseConnect
from data.database_connection import sqlite3
from page.ingredients_and_effects import EffectsPage, IngredientsPage

log = logging.getLogger("alchemy_project_qt.database_management")

class Database:
    def __init__(self, host: str, alchemy_effects: bytes, alchemy_ingredients: bytes, counter: int):
        """
            Initializes the entire database. This goes from checking if the file actually exists (and creating a new
            one if it doesn't) to populate the tables if they were empty.
        :return: None
        """
        log.debug("Initializing database.")
        self.host = host
        log.debug("Checking if the .db file exists.")
        # Check if the file exists at all.
        if not self.check_if_exists():
            log.debug("Creating a database file.")
            with open(self.host, 'w'):
                log.debug("File created.")

        # Checking for the table's content.
        try:
            with DatabaseConnect(self.host) as cursor:
                log.debug("Creating tables if they don't exist.")
                cursor.execute("CREATE TABLE IF NOT EXISTS effects(effect_name TEXT UNIQUE)")
                cursor.execute("CREATE TABLE IF NOT EXISTS ingredients(ingredient_name NAME UNIQUE, ef1 INTEGER, "
                               "ef2 INTEGER, ef3 INTEGER, ef4 INTEGER)")

                log.debug("Seeing if they're empty.")
                cursor.execute("SELECT COUNT(*) FROM effects")
                if cursor.fetchall()[0][0] == 0:
                    log.debug("'effects' table is empty. Populating it...")
                    self.populate_effects(EffectsPage(alchemy_effects))
                    log.debug("Since the effects weren't in store, the potions may not be as well. Populating it...")
                    self.populate_ingredients(IngredientsPage(alchemy_ingredients))
                cursor.execute("SELECT COUNT(*) FROM ingredients")
                if cursor.fetchall()[0][0] == 0:
                    input("The 'effects' are laoded, but the ingredients aren't. Press start to load them.\n")
                    self.populate_ingredients(IngredientsPage(alchemy_ingredients))
        except sqlite3.OperationalError:
            log.critical("A sqlite3.OperationalError was raised.")
            raise
        log.debug("Database successfully initialized.")

    def check_if_exists(self) -> bool:
        """Checks if the database file exists at all.
        :return: True if it does."""
        try:
            with open(self.host, 'r'):
                log.debug("File exists.")
                return True
        except FileNotFoundError:
            log.debug("File doesn't exists.")
            return False

    def populate_effects(self, effects_list: EffectsPage) -> None:
        """
            Deals with populating the 'effects' table. For this, it uses the 'EffectPage' class, since that one manages
            to get a 'row' from the wikitable in the url and call for a 'EffectParser', which deals with each row.
        :return: None
        """
        try:
            log.debug("Writing the list of effects to the 'effects' table in the database.")
            with DatabaseConnect(self.host) as cursor:
                for effect in effects_list.effects:
                    cursor.execute("INSERT INTO effects VALUES(?)", (effect.ef_name,))
            log.debug("Database successfully populated with effects.")
        except sqlite3.OperationalError:
            log.critical("A sqlite3.OperationalError was raised.")

    def populate_ingredients(self, ingredients_list: IngredientsPage) -> None:
        """
            Just as the one for the ingredients, this one deals with populating the 'ingredients' table. In this case,
            this also means to check for the 'effects' table and save the ingredient's effects as their id's in this
            effects table instead of just saving them as a string. I thought this would be a good thing to do and I also
            wanted to see how to do such a thing.
        :param ingredients_list:
        :return: None
        """
        log.debug("Writing ingredients to 'ingredients' table in the database.")
        with DatabaseConnect(self.host) as cursor:
            for ingredient in ingredients_list.ingredients:
                name = ingredient.name
                eff_no = []
                log.debug("Getting the 'id' for the effect from the 'effects' table.")
                for i in range(0, 4):
                    cursor.execute("SELECT ROWID FROM effects WHERE effect_name=?", (ingredient.effects[i],))
                    result = int(cursor.fetchone()[0])
                    eff_no.append(result)
                log.debug("Saving the 'id' for each effect, instead of the entire name.")
                cursor.execute("INSERT INTO ingredients VALUES(?, ?, ?, ?, ?)", (name, eff_no[0], eff_no[1], eff_no[2], eff_no[3]))
            log.debug("Database successfully populated with ingredients.")

    def show_ingredients(self):
        """
            Shows the ingredients and their effects.
        :return: None
        """
        pass

    def show_effects(self, name: str):
        with DatabaseConnect(self.host) as cursor:
            log.debug("Searching for matches in ingredient's name.")
            cursor.execute("SELECT ef1, ef2, ef3, ef4 FROM ingredients WHERE ingredient_name=?", (name, ))
            results = cursor.fetchone()
            if results:
                print(f"Possible effects from {string.capwords(name)} are shown below:")
                for i, effect_no in enumerate(results, start=1):
                    log.debug(f"Searching the effect's name indexed as ¨effect_no={effect_no}¨.")
                    cursor.execute("SELECT effect_name FROM effects WHERE ROWID=?", (int(effect_no),))
                    result = cursor.fetchone()
                    if not any(result):
                        log.critical("There was no match? Seek into the table.")
                    print(f"{i}) {result[0].title()}")
            else:
                log.debug(f"We didn't find any match for the given name ¨{name}¨.")
                print(f"There was no match for the name you provided ({name.title()}). Check your typing.")

    def get_effects_set(self, name: str) -> set:
        with DatabaseConnect(self.host) as cursor:
            log.debug(f"Searching if ¨{name}¨ has a match in 'ingredient_name' within the 'ingredients' table.")
            cursor.execute("SELECT ef1, ef2, ef3, ef4 FROM ingredients WHERE ingredient_name=?", (name, ))
            results = cursor.fetchone()
            if results:
                return {int(effect_no) for effect_no in results}
            else:
                return set()

    def list_effects(self):
        with DatabaseConnect(self.host) as cursor:
            log.debug("Showing a list of effects.")
            cursor.execute("SELECT effect_name FROM effects")
            result = cursor.fetchall()
            for i, (effect,) in enumerate(result, start=1):
                print(f"{i}) {effect.title()}")

    def get_ingredients_for_effect(self, effect_no):
        if not isinstance(effect_no, int):
            log.debug("The effect was given as a string. Finding it's ID...")
            with DatabaseConnect(self.host) as cursor:
                cursor.execute("SELECT ROWID FROM effects WHERE effect_name=?", (effect_no, ))
                result = cursor.fetchone()
                if not result:
                    print(f"There was no match for '{effect_no}'. Check if you spelled it correctly.")
                    return
                else:
                    effect_name = effect_no
                    effect_no = int(result[0])
        log.debug(f"The effect's ID is {effect_no}. We shall now check for ingredients with this effect.")
        with DatabaseConnect(self.host) as cursor:
            cursor.execute("SELECT ingredient_name FROM ingredients WHERE ef1=? OR ef2=? OR ef3=? OR ef4=?", (effect_no, effect_no, effect_no, effect_no))
            result = cursor.fetchall()
            if result:
                for i, (ingredient_name, ) in enumerate(result, start=1):
                    print(f"{i}) {string.capwords(ingredient_name)}.")
            else:
                print("There was no match for such index. Maybe you guessed it out of range?")















