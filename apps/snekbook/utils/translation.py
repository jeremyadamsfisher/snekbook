from typing import Sequence
from unidecode import unidecode
import string


class SnekTranslationImpossible(Exception):
    def __init__(self, disallowed_characters: Sequence[str]):
        self.disallowed_characters = disallowed_characters


eng_to_snek_translation = {
    **{ascii_character: "s" for ascii_character in string.ascii_lowercase},
    **{ascii_character: "S" for ascii_character in string.ascii_uppercase},
}
disallowed_characters = "🐍🍆"


def to_snek(non_snek: str) -> str:
    """translate to snek"""
    disallowed_characters_in_query_phrase = {
        character for character in non_snek if character in disallowed_characters
    }
    if 0 < len(disallowed_characters_in_query_phrase):
        raise SnekTranslationImpossible(disallowed_characters_in_query_phrase)
    return "".join(
        eng_to_snek_translation.get(non_snek_character, non_snek_character)
        for non_snek_character in unidecode(non_snek)
    )
