import logging
from weighted_bingo.file_reader import csv_file_reader
from weighted_bingo.randomizers import place_and_shuffle
from weighted_bingo.output import csv_outputter, echo_outputter

def main():
    items = csv_file_reader.read_from_csv()
    matrix = place_and_shuffle.randomize(items)
    echo_outputter.output(matrix)
    csv_outputter.output(matrix)

if __name__ == '__main__':
    main()