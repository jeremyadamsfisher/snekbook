from typing import Sequence


class SnekTranslationImpossible(Exception):
    def __init__(self, disallowed_characters: Sequence[str]):
        self.disallowed_characters = disallowed_characters


lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
same = """,.!'";!-() —"""
eng_to_snek_translation = dict(zip(same, same))
for alphabet, m in [(lower, "s"), (upper, "S")]:
    for c in alphabet:
        eng_to_snek_translation[c] = m


def to_snek(non_snek: str) -> str:
    """translate from english to snek"""
    try:
        return "".join(eng_to_snek_translation[c] for c in non_snek)
    except KeyError:
        raise SnekTranslationImpossible(
            {c for c in non_snek if c not in eng_to_snek_translation}
        )
