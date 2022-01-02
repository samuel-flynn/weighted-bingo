import logging
from math import floor
from random import randint
from typing import List

from weighted_bingo.model.bingo_item import BingoItem

__logger = logging.getLogger(__name__)

def get_item_pool(items : List[BingoItem]):

    pool = []

    total_average = __calculate_total_average(items)

    available_indexes = list(range(len(items)))
    
    for i in range(24):
        pick_index = randint(0, len(available_indexes) - 1)
        pick_val = available_indexes[pick_index]
        pool.append(items[pick_val])

        available_indexes.remove(pick_val)
    
    __logger.info(f'Logger pool average: {total_average}')
    
    return pool



def __calculate_total_average(items : List[BingoItem]):

    count = 0
    sum = 0
    for bingo_item in items:
        count += 1
        sum += bingo_item.weight
    
    if count == 0:
        return 0

    return floor(sum * 24 / count)
