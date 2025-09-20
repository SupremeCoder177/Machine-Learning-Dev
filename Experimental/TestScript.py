from CsvReader import CsvReader as Reader

file = Reader().read("F:\\Machine Learning\\Datasets\\CSV Files\\test.csv", ",")
print(file.get(0))
print(file.get_column("Name"))

