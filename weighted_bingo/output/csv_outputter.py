import csv
import logging
import os
from weighted_bingo import resources_dir
from weighted_bingo.model.bingo_matrix import BingoMatrix
from weighted_bingo.model.bingo_row import BingoRow

__logger = logging.getLogger(__name__)

def output(matrix : BingoMatrix):

    with open(os.path.join(resources_dir, 'card.csv'), 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file, delimiter = ',')
        for i in range(5):
            row = __get_csv_row(matrix[i])
            csv_writer.writerow(row)

def __get_csv_row(row : BingoRow):
    csv_row = []

    for cell in row:
        csv_row.append(cell.name)

    return csv_row
