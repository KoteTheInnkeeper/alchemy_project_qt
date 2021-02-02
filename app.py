import requests

from data.database_management import Database
from page.ingredients_and_effects import EffectsPage

# Set the database
data = Database('data/data.db')

# Get the page content for the effects
page_content = requests.get('https://en.uesp.net/wiki/Skyrim:Alchemy_Effects').content
page = EffectsPage(page_content)

for effect in page.effects:
    print(effect.ef_name)
