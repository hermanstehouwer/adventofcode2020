import copy
from typing import List, Set


class Player:
    cards: List[int]
    number: int
    winner: bool

    def __init__(self, cards: str):
        self.cards = []
        lines = cards.split("\n")
        self.number = int(lines.pop(0)[-2])
        self.winner = False
        for line in lines:
            self.cards.append(int(line))

    def score(self) -> int:
        score = 0
        for i, card in enumerate(reversed(self.cards)):
            score += (i+1)*card
        return int(self.winner) * score

    def gameover(self):
        return len(self.cards) == 0

    def play_card(self):
        return self.cards.pop(0)

    def won_cards(self, draw: List[int], first: int):
        self.cards.append(draw.pop(first))
        self.cards.extend(draw)

    def __str__(self):
        return ",".join(str(c) for c in self.cards)


class CardGame:
    players: List[Player]

    def __init__(self, decks: List[str]):
        self.players = []
        for deck in decks:
            self.players.append(Player(deck))

    def handle_regular_round(self, draw):
        winning_card = max(draw)
        winning_player = draw.index(winning_card)
        self.players[winning_player].won_cards(draw, winning_player)

    def handle_recursive_round(self, draw):
        recurse_game: CardGame = self.get_copy_with_cards(draw)
        recurse_game.play_recursive()
        winning_player = recurse_game.idx_of_winner()
        self.players[winning_player].won_cards(draw, winning_player)

    def play(self):
        while not self.gameover():
            draw = [p.play_card() for p in self.players]
            self.handle_regular_round(draw)
        self.mark_winner()

    def play_recursive(self):
        previous: Set[str] = set()
        while not self.gameover():
            # If exactly same round before instantly end
            if self.to_compare_string() in previous:
                return self.sudden_end()
            previous.add(self.to_compare_string())

            # begin round by drawing as normal
            draw = [p.play_card() for p in self.players]
            # If not enough cards: winner as normal
            if not self.all_have_enough_cards(draw):
                self.handle_regular_round(draw)
                continue

            # Time to recurse!
            self.handle_recursive_round(draw)
        self.mark_winner()

    def get_winning_score(self):
        return max(p.score() for p in self.players)

    def gameover(self):
        return any([p.gameover() for p in self.players])

    def sudden_end(self):
        self.players[0].winner = True

    def mark_winner(self):
        for p in self.players:
            if len(p.cards) > 0:
                p.winner = True

    def idx_of_winner(self):
        for i, p in enumerate(self.players):
            if p.winner:
                return i

    def all_have_enough_cards(self, draw) -> bool:
        return all(len(self.players[i].cards) >= card for i, card in enumerate(draw))

    def get_copy_with_cards(self, draw: List[int]):
        ret = copy.deepcopy(self)
        for i, c in enumerate(draw):
            ret.players[i].cards = ret.players[i].cards[:c]
        return ret

    def to_compare_string(self) -> str:
        return '|'.join([str(p) for p in self.players])

