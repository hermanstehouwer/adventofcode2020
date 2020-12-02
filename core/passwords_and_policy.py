from abc import abstractmethod, ABC


class PasswordPolicy(ABC):
    min: int
    max: int
    letter: str

    def __init__(self, policy_string: str):
        occurrences, self.letter = policy_string.split(' ')
        min, max = occurrences.split('-')
        self.min = int(min)
        self.max = int(max)

    @abstractmethod
    def check_password_against_policy(self, password: str) -> bool:
        pass


class SledRentalPolicy(PasswordPolicy, ABC):
    def check_password_against_policy(self, password: str) -> bool:
        count = password.count(self.letter)
        return self.min <= count <= self.max


class OfficialTobogganPolicy(PasswordPolicy, ABC):
    def check_password_against_policy(self, password: str) -> bool:
        return (password[self.min-1] == self.letter) ^ (password[self.max-1] == self.letter)
