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
        if count < self.min or count > self.max:
            return False
        return True


class OfficialTobogganPolicy(PasswordPolicy, ABC):
    def check_password_against_policy(self, password: str) -> bool:
        hitcount = 0
        for check_index in [self.min, self.max]:
            if len(password) >= check_index and password[check_index-1] == self.letter:
                hitcount += 1
        return hitcount == 1
