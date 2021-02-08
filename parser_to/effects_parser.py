import re

from locators.effects_locator import EffLoc


class EffectParser:
    def __init__(self, parent):
        self.parent = str(parent)

    @property
    def ef_name(self):
        regex = EffLoc.RE_NAME
        matches = re.search(regex, self.parent)
        return matches.group(1).lower()



