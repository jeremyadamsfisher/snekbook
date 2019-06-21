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

def to_snek(non_snek: str) -> str:
    """translate from non-snek to snek"""
    try:
        return "".join(
            eng_to_snek_translation.get(non_snek_character, non_snek_character)
            for non_snek_character in unidecode(non_snek)
        )
    except KeyError:
        raise SnekTranslationImpossible(
            {c for c in non_snek if c not in eng_to_snek_translation}
        )
