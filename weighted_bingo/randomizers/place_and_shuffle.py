import logging
from typing import Any, List

from weighted_bingo.model.bingo_item import BingoItem
from weighted_bingo.model.bingo_matrix import BingoMatrix
from weighted_bingo.randomizers.item_pool_creator import get_item_pool

__logger = logging.getLogger(__name__)

def randomize(items : List[BingoItem]) -> BingoMatrix:
    matrix = BingoMatrix()

    items_counter = 0
    item_pool = get_item_pool(items)

    for row_index in range(5):
        for column_index in range(5):
            if row_index == 2 and column_index == 2:
                matrix[row_index][column_index] = BingoItem('Free Space', 0)
                continue

            matrix[row_index][column_index] = item_pool[items_counter]
            items_counter += 1

    return matrix