class Seat:
    row: int
    column: int

    def __init__(self, boarding_pass):
        boarding_pass = boarding_pass.translate(
            str.maketrans("FBLR", "0101")
        )
        self.row = int(boarding_pass[0:-3], 2)
        self.column = int(boarding_pass[-3:], 2)

    def get_ID(self):
        return self.row * 8 + self.column

