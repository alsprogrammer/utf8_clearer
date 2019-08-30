from abc import ABC, abstractmethod
from utf8clearer.cleaners import Clearer
from io import RawIOBase


class Processor(ABC):
    @abstractmethod
    def __call__(self, source, destination):
        pass


class StreamProcessor(Processor):
    def __init__(self, clearer: Clearer):
        self._clearer = clearer

    def __call__(self, source: RawIOBase, destination: RawIOBase):
        for element in source:
            destination.write(self._clearer(element))
