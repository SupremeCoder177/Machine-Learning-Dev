from typing import List

class InvalidInput(Exception):
    def __init__(self, msg): pass


class CsvFile:

    def __init__(self):
        self.data = list()
        self.headings = None

    def get(self, row) -> None | dict:
        if 0 <= row <= len(self.data):
            return self.data[row]
        return None

    def get_column(self, heading : str) -> List[any]:
        tmp = []
        for row in self.data:
            tmp.append(row[self.headings.index(heading)])
        return tmp

    def add(self, row : dict, header : bool) -> None:
        if self.check_valid_row_input(row):
            if header:
                self.headings = row

            if not header and self.headings:
                self.data.append(row)
        else:
            raise InvalidInput("Invalid data")

    def check_valid_row_input(self, row : dict) -> bool:
        if len(row) != len(self.data[0]): return False
        for i in range(len(row)):
            if type(row[i]) != type(self.data[1][i]):
                return False
        return True