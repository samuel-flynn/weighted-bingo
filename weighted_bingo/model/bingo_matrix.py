import logging
from typing import List

from weighted_bingo.model.bingo_row import BingoRow

class BingoMatrix:

    __rows : List[BingoRow]

    def __init__(self) -> None:
        self.__rows = [BingoRow(), BingoRow(), BingoRow(), BingoRow(), BingoRow()]

    def __iter__(self):
        return BingoMatrixIter(self)
    
    def __getitem__(self, index : int) -> BingoRow:
        return self.__rows[index]
    
    def __setitem__(self, index : int, row : BingoRow) -> None:
        self.__rows[index] = row
    
    def __delitem__(self, index : int) -> BingoRow:
        del(self.__rows[index])

    def __len__(self) -> int:

        return len(self.__rows)

    def column_weight(self, column_index : int) -> int:
        
        column_sum = 0

        for row in self:

            column_sum += row[column_index].weight
        
        return column_sum

    def descending_diag_weight(self) -> int:

        diag_sum = 0
        column_index = 0

        for row in self:
            diag_sum += row[column_index].weight
            column_index += 1

        return diag_sum

    def ascending_diag_weight(self) -> int:

        diag_sum = 0
        column_index = len(self) - 1

        for row in self:
            diag_sum += row[column_index].weight
            column_index -= 1

        return diag_sum
    
    def total_weight(self) -> int:

        big_sum = 0

        for row in self:
            big_sum += row.row_weight()
        
        return big_sum

class BingoMatrixIter:

    __iter_index : int
    __matrix : BingoMatrix

    def __init__(self, matrix) -> None:
        self.__iter_index = 0
        self.__matrix = matrix

    def __next__(self) -> BingoRow:
        if self.__iter_index >= len(self.__matrix):
            raise StopIteration()

        next = self.__matrix[self.__iter_index]
        self.__iter_index += 1

        return next