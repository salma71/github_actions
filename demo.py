from typing import List
import random

def random_sampling(k: int, array_list: List[int]) -> None:
    """[summary]

    Args:
        k (int): [description]
        A (List[int]): [description]
    """
    for i in range(k):
        random_index = random.randint(i, len(array_list) - 1)
        # swap element based on the generated index
        array_list[i], array_list[random_index] = array_list[random_index], array_list[i]
