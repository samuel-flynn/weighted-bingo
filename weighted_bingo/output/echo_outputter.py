import logging

from weighted_bingo.model.bingo_matrix import BingoMatrix

__logger = logging.getLogger(__name__)
__width = 20
def output(matrix : BingoMatrix):
    for row_index in range(len(matrix)):
        row = matrix[row_index]
        row_text = ''
        for column in row:
            row_text += f'| {__elide(column).ljust(__width)} '
        
        row_text += f'| {row.row_weight()} '

        if row_index == 0:
            row_text += f'| {matrix.ascending_diag_weight()}'
        
        if row_index == len(matrix) - 1:
            row_text += f'| {matrix.descending_diag_weight()}'

        __logger.info(row_text)

    footer_row = ''
    for column_index in range(len(matrix[0])):
        footer_row += f'| {__elide(matrix.column_weight(column_index)).ljust(__width)} '
    
    footer_row += f'| {matrix.total_weight()}'

    __logger.info(footer_row)

def __elide(to_elide):
    to_elide_str = str(to_elide)
    return to_elide_str[:__width - 3] + '...' if len(str(to_elide_str)) > __width else to_elide_str
