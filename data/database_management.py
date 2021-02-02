"""
    This file aims to work over the database. It creates a 'Database' object with it's own methods to getting the
    info we want.
"""
import logging

from data.database_connection import DatabaseConnection as DatabaseConnect
from data.database_connection import sqlite3
from page.ingredients_and_effects import EffectsPage


# Set the basic configurations for the logger
logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s", level=logging.DEBUG,
                    filename='log.txt')
# Create the logger
logger = logging.getLogger("'Alchemy project' logger.")


class Database:
    def __init__(self, host: str, alchemy_effects: bytes, alchemy_ingredients: bytes):
        """
            Initializes the entire database. This goes from checking if the file actually exists (and creating a new
            one if it doesn't) to populate the tables if they were empty.
        :return: None
        """
        logger.debug("Initializing database.")
        self.host = host
        logger.debug("Checking if the .db file exists.")
        # Check if the file exists at all.
        try:
            with open(self.host, 'r'):
                logger.debug("File exists. Checking for the table's content.")
        except FileNotFoundError:
            with open(self.host, 'w'):
                logger.debug("File didn't exist. A new one was created.")

        # Checking for the table's content.
        try:
            with DatabaseConnect(self.host) as cursor:
                logger.debug("Creating tables if they don't exist.")
                cursor.execute("CREATE TABLE IF NOT EXISTS effects(effect_name TEXT UNIQUE)")
                cursor.execute("CREATE TABLE IF NOT EXISTS ingredients(ingredient_name NAME UNIQUE, ef1 INTEGER, "
                               "ef2 INTEGER, ef3 INTEGER, ef4 INTEGER)")

                logger.debug("Seeing if they're empty.")
                cursor.execute("SELECT COUNT(*) FROM effects")
                if cursor.fetchall()[0][0] == 0:
                    input("It appears that the info wasn't downloaded. Press enter to download the potions info.\n")
                    logger.debug("'effects' table is empty. Populating it...")
                    self.populate_effects(EffectsPage(alchemy_effects))
                    logger.debug("Since the effects weren't in store, the potions may not be as well. Populating it...")
                    self.populate_ingredients()
                cursor.execute("SELECT COUNT(*) FROM ingredients")
                if cursor.fetchall()[0][0] == 0:
                    self.populate_ingredients()
        except sqlite3.OperationalError:
            logger.critical("A sqlite3.OperationalError was raised.")
            raise

    def populate_effects(self, effects_list: EffectsPage) -> None:
        try:
            with DatabaseConnect(self.host) as cursor:
                for effect in effects_list.effects:
                    cursor.execute("INSERT INTO effects VALUES(?)", (effect.ef_name,))
        except sqlite3.OperationalError:
            logger.critical("A sqlite3.OperationalError was raised.")

    def populate_ingredients(self) -> None:
        pass





