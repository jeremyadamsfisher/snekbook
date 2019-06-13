from typing import Sequence
import itertools

def grouped(l: Sequence, n: int):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def to_snek(non_snek) -> str:
    lower = "abcdefghijklmnoqrstuvwxyz"
    upper = lower.upper()
    same = " ,.!"
    mapping = dict(zip(same, same))
    for alphabet, m in [(lower, "s"), (upper, "S")]:
        for c in alphabet:
            mapping[c] = m
    return "".join(mapping[c] for c in non_snek)