import re
from bs4 import BeautifulSoup
from locators.ingredients_locator import IngLocators


class IngredientParser:
    """
        This class deals with each row, turning them into valuable info. In this particular case, we
        got ourselves an ingredient and their effects by doing this.
    """

    def __init__(self, parent: str):
        self.parent: BeautifulSoup = BeautifulSoup(parent, 'html.parser')

    @property
    def name(self):
        locator = IngLocators.COLUMN_ELEMENT_LOCATOR
        row_elements_tag = self.parent.select(locator)
        name = row_elements_tag[0].string.lower()
        return name

    @property
    def effects(self):
        locator = IngLocators.COLUMN_ELEMENT_LOCATOR
        row_elements_tag = self.parent.select(locator)
        # There's a row that has two 'a' tags in the 'name' column for the ingredient. In the page, this row is also
        # the only one with 9 'a' tags, so I'm using that to detect when we're passed down that row and erasing this
        # undesired 'a' tag.
        if len(row_elements_tag) == 9:
            row_elements_tag.pop(0)
        regex = IngLocators.RE_EFFECT
        return tuple(
            re.findall(regex, str(e))[0].lower()
            for i, e in enumerate(row_elements_tag)
            if i in range(1, 5)
        )

    def __repr__(self):
        return f"<{self.name}> ingredient with <{self.effects}>."

    def __str__(self):
        string_to_print = f'{self.name.title()} effects are shown below:\n'
        for effect in self.effects:
            string_to_print += f'\t -> {effect}\n'



