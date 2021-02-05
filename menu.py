"""
    The entire user-interface with the command line will be here.
"""
import logging

from app import data

WELCOME_STRING = """Welcome to this alchemy_project program for Skyrim."""
COMMANDS_STRING = """The following commands are valid:

'i' - to enter a name and know it's effects.
'r' - to get a recipe for a specific effect.
'q' - to quit the program."""

# Set the logger
logger = logging.getLogger('/alchemy_project/menu')


class Operations:
    @classmethod
    def get_effects(cls):
        ingredient_name = input("Give me the ingredient's name: ").strip().lower()
        data.show_effects(ingredient_name)

    @classmethod
    def exit_program(cls):
        print("Thanks for using this program!")
        exit()

    @classmethod
    def show_help(cls):
        print(COMMANDS_STRING)

    @classmethod
    def get_ingredients(cls):
        print("The effects available are shown below:")
        data.list_effects()
        print("Now, you can tell me which potion you want to brew by matching it's effect's name or by index according"
              " to the list above.")
        user_input = input("Your choice: ").strip().lower()
        try:
            user_input = int(user_input)
            data.get_ingredients_for_effect(user_input)
        except ValueError:
            logger.debug(f"Searching for ingredients to achieve the ¨{user_input}¨ effect. ")
            data.get_ingredients_for_effect(user_input)


def main_menu():
    logger.debug("Running the main menu")
    OPERATIONS = {
        'i': Operations.get_effects,
        'q': Operations.exit_program,
        'r': Operations.get_ingredients,
        'h': Operations.show_help
    }
    user_input = input("\nEnter a command: ").strip().lower()
    try:
        to_perform = OPERATIONS[user_input]
        logger.debug(f"Performing the ¨{to_perform.__name__}¨ operation.")
        to_perform()
    except KeyError:
        logger.warning("The user entered an invalid input.")
        print("That's not a valid input. Try again. If you need help, enter the 'h' command to see the valid commands.")


print(WELCOME_STRING)
print(COMMANDS_STRING)
_ = True
while _:
    main_menu()
