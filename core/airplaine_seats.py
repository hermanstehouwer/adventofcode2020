class Seat:
    ID: int
    def __init__(self, boarding_pass):
        boarding_pass = boarding_pass.translate(
            str.maketrans("FBLR", "0101")
        )
        self.ID = int(boarding_pass, 2)
