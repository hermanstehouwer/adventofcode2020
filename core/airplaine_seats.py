class Seat:
    row: int
    column: int

    def __init__(self, boarding_pass):
        row_desc = boarding_pass[0:-3].translate(str.maketrans("FB", "01"))
        self.row = int(row_desc, 2)

        column_desc = boarding_pass[-3:].translate(str.maketrans("LR", "01"))
        self.column = int(column_desc, 2)

    def get_ID(self):
        return self.row * 8 + self.column

