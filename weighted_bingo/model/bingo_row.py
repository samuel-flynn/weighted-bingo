from typing import List
from weighted_bingo.model.bingo_item import BingoItem

class BingoRow:

    __cells : List[BingoItem]
    __iter_index : int

    def __init__(self) -> None:
        self.__cells = [None, None, None, None, None]

    def __iter__(self):
        return BingoRowIter(self)
    
    def __next__(self) -> BingoItem:
        if self.__iter_index >= len(self.__cells):
            raise StopIteration()

        next = self.__cells[self.__iter_index]
        self.__iter_index += 1

        return next
    
    def __getitem__(self, index : int) -> BingoItem:
        return self.__cells[index]
    
    def __setitem__(self, index : int, item : BingoItem) -> None:

        self.__cells[index] = item

    def __delitem__(self, index : int) -> None:

        del(self.__cells[index])

    def __len__(self) -> int:

        return len(self.__cells)
    
    def row_weight(self) -> int:

        row_sum = 0

        for cell in self:
            row_sum += cell.weight
        
        return row_sum

class BingoRowIter:

    __iter_index : int
    __row : BingoRow

    def __init__(self, row) -> None:
        self.__iter_index = 0
        self.__row = row

    def __next__(self) -> BingoItem:
        if self.__iter_index >= len(self.__row):
            raise StopIteration()

        next = self.__row[self.__iter_index]
        self.__iter_index += 1

        return next