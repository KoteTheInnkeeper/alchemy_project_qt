from bs4 import BeautifulSoup4
from locators.ingredients_locator import IngLocators

class IngredientParser:
    """
        This class deals with each row, turning them into valuable info. In this particular case, we
        got ourselves an ingredient and their effects by doing this.
    """

    def __init__(self, parent: bytes):
        self.parent = BeautifulSoup4(parent, 'html.parser')

    @property
    def name(self):
        locator = IngLocators.COLUMN_ELEMENT_LOCATOR
        row_elements_tag = self.parent.select(locator)
        return [BeautifulSoup(e,'html.parser')]