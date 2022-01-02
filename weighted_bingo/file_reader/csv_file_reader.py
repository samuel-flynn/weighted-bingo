from weighted_bingo import resources_dir
import os
import csv
import logging

from weighted_bingo.model.bingo_item import BingoItem

__logger = logging.getLogger(__name__)

def read_from_csv():
    items = []
    with open(os.path.join(resources_dir, 'items.csv'), 'r') as items_file:
        reader = csv.reader(items_file, delimiter=',', quotechar='|')
        for row in reader:
            #__logger.info(f'{row[0]}: {row[1]}')
            if len(row) != 2:
                raise ValueError(f'Error with row: {str(row)}. Expected 2 tokens, got {len(row)}.')
            if not row[1].isnumeric():
                raise ValueError(f'Error with row: {str(row)}. Second token should be numeric.')
                
            items.append(BingoItem(row[0], int(row[1])))

    return items