import re
from bs4 import BeautifulSoup
from locators.ingredients_locator import IngLocators
from data.database_connection import DatabaseConnection as DatabaseConnect


class IngredientParser:
    """
        This class deals with each row, turning them into valuable info. In this particular case, we
        got ourselves an ingredient and their effects by doing this.
    """

    def __init__(self, parent: str):
        self.parent = BeautifulSoup(parent, 'html.parser')

    @property
    def name(self):
        locator = IngLocators.COLUMN_ELEMENT_LOCATOR
        row_elements_tag = self.parent.select(locator)
        return row_elements_tag[0].string

    @property
    def effects(self):
        locator = IngLocators.COLUMN_ELEMENT_LOCATOR
        row_elements_tag = self.parent.select(locator)
        regex = IngLocators.RE_EFFECT
        return tuple(
            re.findall(regex, str(e))[0]
            for i, e in enumerate(row_elements_tag)
            if i in range(1, 5)
        )

    def __str__(self):
        return f"{self.name} has the following effects: {self.effects[0]}, {self.effects[1]}, {self.effects[2]} and" \
               f" {self.effects[3]}."


if __name__ == '__main__':
    string_to_test = """
<tr>
<td><a href="/wiki/Abecean_Longfin" title="Abecean Longfin">Abecean Longfin</a>
</td>
<td><a href="/wiki/Weakness_to_Frost_(Skyrim)" title="Weakness to Frost (Skyrim)">Weakness to Frost</a>
</td>
<td><a href="/wiki/Fortify_Sneak" title="Fortify Sneak">Fortify Sneak</a>
</td>
<td><a href="/wiki/Weakness_to_Poison_(Skyrim)" title="Weakness to Poison (Skyrim)">Weakness to Poison</a>
</td>
<td><a href="/wiki/Fortify_Restoration" title="Fortify Restoration">Fortify Restoration</a>
</td>
<td>0.5
</td>
<td>15
</td>
<td>Lakes, rivers, streams, fish barrels
</td></tr>"""

    first_ingredient = IngredientParser(string_to_test)
    print(first_ingredient)
