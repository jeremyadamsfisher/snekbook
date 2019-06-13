from typing import Sequence

def grouped(l: Sequence, n: int):
    for i in range(0, len(l), n):
        yield l[i:i+n]