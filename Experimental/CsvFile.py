from typing import List

class InvalidInput(Exception):
    def __init__(self, msg): pass


class NoHeader(Exception):
    def __int__(self, msg): pass

class InvalidHeaderFormat(Exception):
    def __init__(self, msg): pass


class CsvFile:

    def __init__(self):
        self.data = list()
        self.headings = None

    def get(self, row) -> None | dict:
        if 0 <= row < len(self.data):
            return self.data[row]
        return None

    def get_column(self, heading : str) -> List[any]:
        tmp = []
        index = list(self.headings.keys()).index(heading)
        for row in self.data:
            tmp.append(row[index])
        return tmp

    def add(self, row : dict | list, header : bool) -> None:
        if header and isinstance(row, dict):
            self.headings = row
            return

        if header and not isinstance(row, dict):
            raise InvalidHeaderFormat("The header should be a dictionary")

        if not self.headings:
            raise NoHeader("No header set for file")

        if self.check_valid_row_input(row):
            if not header and self.headings:
                self.data.append(row)
        else:
            raise InvalidInput("Invalid data")

    def check_valid_row_input(self, row : dict) -> bool:
        if len(row) != len(self.headings): return False
        for i in range(len(row)):
            if type(row[i]) != list(self.headings.values())[i]:
                return False
        return True