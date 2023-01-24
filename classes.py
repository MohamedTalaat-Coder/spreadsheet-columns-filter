import pandas as pd

class Excel:

    def __init__(self, file):
        self.file = file
        try:
            self.file = pd.read_excel(self.file)
        except FileNotFoundError:
            raise FileNotFoundError("File Not Found")
    def __str__(self) -> str:
        return f"{self.file}"
        

    def show_columns(self):
        for col in self.file.columns:
            print(col)
        print()
        column = input("Column: ")
        try:
            return self.file[column].unique()
        except KeyError:
            raise KeyError("Invalid Column Name.")
