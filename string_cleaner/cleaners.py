from abc import ABC, abstractmethod


class Cleaner(ABC):
    @abstractmethod
    def __call__(self, object_to_clear):
        pass


class StringCleaner(Cleaner):
    def __init__(self, allowed_chars: str):
        self._allowed_chars = allowed_chars

    def __call__(self, string_to_clear: str):
        return ''.join(x for x in string_to_clear if x in self._allowed_chars)
