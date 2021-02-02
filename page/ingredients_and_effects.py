from bs4 import BeautifulSoup
from locators.effects_locator import EffPageLoc
from parser.effects_parser import EffectParser


class EffectsPage:
    def __init__(self, page: bytes) -> None:
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def effects(self):
        locator = EffPageLoc.EFF_ROW
        ingredient_tags = self.soup.select(locator)
        for _ in range(0, 2):
            ingredient_tags.pop(0)
        return [
            EffectParser(e)
            for e in ingredient_tags
            if EffectParser(e).ef_name != ''
        ]

