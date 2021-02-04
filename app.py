import requests

from data.database_management import Database, logger


# Get the page content for the effects and ingredients
alchemy_effects_content = requests.get('https://en.uesp.net/wiki/Skyrim:Alchemy_Effects').content
alchemy_ingredients_content = requests.get('https://elderscrolls.fandom.com/wiki/Ingredients_(Skyrim)').content

# Set the database
data = Database('data/data.db', alchemy_effects_content, alchemy_ingredients_content)
