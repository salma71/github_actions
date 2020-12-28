import functools
from typing import List
import random

def random_sampling(k: int, A: List[int]) -> None:
    for i in range(k):
        random_index = random.randint(i, len(A) - 1)
        # swap element based on the generated index
        A[i], A[random_index] = A[random_index], A[i]
