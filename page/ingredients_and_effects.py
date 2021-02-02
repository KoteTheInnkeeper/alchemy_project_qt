from bs4 import BeautifulSoup
from locators.effects_locator import EffPageLoc
from locators.ingredients_locator import IngLocators
from parser.effects_parser import EffectParser
from parser.ingredients_parser import IngredientParser


class EffectsPage:
    """
        This type of object will have two properties: one assigned as initialization (a BeautifulSoup4 object) and
        another one which holds a list of 'EffectParser' objects. This ones have a 'ef_name' property for each effect's
        name.
    """
    def __init__(self, page: bytes) -> None:
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def effects(self):
        locator = EffPageLoc.EFF_ROW
        effect_tags = self.soup.select(locator)
        for _ in range(0, 2):
            effect_tags.pop(0)
        return [
            EffectParser(e)
            for e in effect_tags
            if EffectParser(e).ef_name != ''
        ]


class IngredientsPage:
    """
        Same thing as with the effects, but this is done to the ingredients.
    """
    def __init__(self, page: bytes) -> None:
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def ingredients(self) -> list:
        locator = IngLocators.ROW_LOCATOR
        row_tags = self.soup.select(locator)
        return [
            IngredientParser(e)
            for e in row_tags
        ]
