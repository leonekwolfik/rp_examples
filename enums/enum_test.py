from enum import Enum
import string


class BaseTextEnum(Enum):
    def as_list(self):
        try:
            return list(self.value)
        except TypeError:
            return [str(self.value)]


class Alphabet(BaseTextEnum):
    LOWERCASE = string.ascii_lowercase
    UPPERCASE = string.ascii_lowercase


print(Alphabet.LOWERCASE.as_list())
