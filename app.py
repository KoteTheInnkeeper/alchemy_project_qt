import logging

# Setting the logger
# Set the basic configurations for the logger
logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s", level=logging.DEBUG,
                    filename='log.log')
# Create the logger
logger = logging.getLogger("alchemy_project_qt.app")


import requests

from data.database_management import Database


# Get the page content for the effects and ingredients
alchemy_effects_content = requests.get('https://en.uesp.net/wiki/Skyrim:Alchemy_Effects').content
alchemy_ingredients_content = requests.get('https://elderscrolls.fandom.com/wiki/Ingredients_(Skyrim)').content

# Set the database
data = Database('data/data.db', alchemy_effects_content, alchemy_ingredients_content)
