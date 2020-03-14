from typing import Dict


class CharacterCounter:

    def __init__(self):
        self.characters: Dict[str, int] = {}

    def __repr__(self) -> str:
        return str(self.characters)

    def add_text(self, data: str):
        """
        Adds the given text to this character counter, processing it

        Parameters:
            data: the text to be counted
        """
        for char in data:
            if char not in self.characters.keys():
                self.characters[char] = 1
            else:
                self.characters[char] += 1

    def get_characters(self) -> Dict[str, int]:
        """
        Gets the dictionary of each character and it's associated count.

        Return:
            a dicitionary of each character and the number of times it has occurred in the string.
        """
        return self.characters

    def occurences(self, char: str) -> int:
        """
        Returns the number of times the given character appeared in the messages

        Parameters:
            char: the character to get the occurences of

        Return:
            the number of times char appeared in the string.
        """
        result = 0
        if(char in self.characters.keys()):
            result = self.characters[char]
        return result
