from CsvFile import CsvFile
import os
from typing import List

class IncorrectExtension(Exception):
    def __init__(self, msg): pass


class InvalidDelimeter(Exception):
    def __init__(self, msg): pass


def get_line(file_path : str, start_index : int, return_last_index : bool) -> str:
    output = str()
    index = start_index
    with open(file_path, "r") as f:
        temp = f.read()
        while temp[index] != '\n':
            output += temp[index]
            index += 1
    return output if not return_last_index else output, index + 1


class CsvReader:

    def __init__(self):
        self.delimeters = [",", ".", ":", " ", "_", "-"]
        self.index = 0

    def read(self, file_path : str, delimeter = ",") -> CsvFile:
        if not os.path.exists(file_path):
            raise FileNotFoundError("No such file or directory")

        if not os.path.isfile(file_path):
            raise FileNotFoundError("No such file")

        if not os.path.split(file_path)[1].endswith(".csv"):
            raise IncorrectExtension("The file extension must be .csv")

        if delimeter not in self.delimeters:
            raise InvalidDelimeter("The delimeter passed is not valid")

        tmp = CsvFile()
        max_len = 0
        with open(file_path, 'r') as f:
            max_len = len(f.read())

        self.index = 0
        self.parse(file_path, tmp, delimeter, max_len)
        return tmp

    def parse(self, fp : str, tmp : CsvFile, delimeter : str, max_len : int) -> None:
        headings_line, self.index = get_line(fp, self.index, True)
        cells_line, self.index = get_line(fp, self.index, True)
        headings = self.tokenize(headings_line, delimeter)
        cells = self.tokenize(cells_line, delimeter)

        temp = dict()
        for heading, cell in zip(headings, cells):
            temp[heading] = type(cell)

        tmp.add(temp, True)
        tmp.add(cells, False)
        while self.index < max_len:
            line, self.index = get_line(fp, self.index, True)
            tokens = self.tokenize(line, delimeter)
            tmp.add(tokens, False)

    def tokenize(self, text : str, delimeter : str) -> List[any]:
        tokens = text.strip().split(delimeter)
        for i in range(len(tokens)):
            try:
                temp = int(tokens[i])
                tokens[i] = temp
            except ValueError as e:
                continue
        return tokens




# with open("..\\Datasets\\CSV Files\\test.csv", "r") as f:
#     for ch in f.read():
#         print(ch)
