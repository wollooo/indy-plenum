from abc import ABC, abstractmethod
from random import Random
from typing import Any, Iterable, List


class SimRandom(ABC):
    @abstractmethod
    def integer(self, min_value: int, max_value: int) -> int:
        pass

    @abstractmethod
    def choice(self, *args) -> Any:
        pass

    @abstractmethod
    def sample(self, population: List, num: int) -> List:
        pass

    @abstractmethod
    def shuffle(self, items: List) -> List:
        pass


class DefaultSimRandom(SimRandom):
    # TODO: Consider making seed fixed to make it always deterministic
    def __init__(self, seed=None):
        self._random = Random(seed)

    def integer(self, min_value: int, max_value: int) -> int:
        return self._random.randint(min_value, max_value)

    def choice(self, *args) -> Any:
        return self._random.choice(args)

    def sample(self, population: Iterable, num: int) -> List:
        return self._random.sample(population, num)

    def shuffle(self, items: List) -> List:
        result = items.copy()
        self._random.shuffle(result)
        return result
