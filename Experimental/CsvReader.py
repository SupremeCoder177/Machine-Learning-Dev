from CsvFile import CsvFile
import os
from typing import List

class IncorrectExtension(Exception):
    def __init__(self, msg): pass


class InvalidDelimeter(Exception):
    def __init__(self, msg): pass


class CsvReader:

    def __init__(self):
        self.delimeters = [",", ".", ":", " ", "_", "-"]

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
        with open(file_path, "r") as f:
            self.parse(f.read(), tmp, delimeter)
        return tmp

    def parse(self, data : str, tmp : CsvFile, delimeter : str) -> None:
        index = 0
        limit = len(data)
        header = True
        while index < limit:
            print('parsing...')
            row = self.get_row(index, data, delimeter)
            if isinstance(row, list):
                tmp.add(row[0], header)
                index = row[1]
            else:
                index = row
            if header: header = False

    def get_row(self, start_index: int, text: str, delimeter: str) -> List[any] | None:
        output = []
        index = start_index
        while text[index] != "\n" or text[index] != "\0":
            tmp =  self.get_next(text, start_index, delimeter)
            if isinstance(tmp, list):
                output.append(tmp[0])
                index = tmp[1]
            else:
                index = tmp
        return [output, index] if len(output) != 0 else index

    @staticmethod
    def get_next(txt : str, index : int, delimeter : str) -> List[any] | int:
        output = ""
        while True:
            if txt[index] == delimeter or txt[index] == '\n' or txt[index] == '\0': break
            output += txt[index]
            index += 1
        return [output, index] if output != "" else index