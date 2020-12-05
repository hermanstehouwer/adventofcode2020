class Seat:
    row: int
    column: int

    def __init__(self, boarding_pass):
        # row
        row_desc = boarding_pass[0:-3]
        row_desc = row_desc.replace("F", "0").replace("B", "1")
        self.row = int(row_desc, 2)

        # column
        column_desc = boarding_pass[-3:]
        column_desc = column_desc.replace("L", "0").replace("R", "1")
        self.column = int(column_desc, 2)

    def get_ID(self):
        return self.row * 8 + self.column

