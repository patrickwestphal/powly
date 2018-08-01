from abc import ABC, abstractmethod


class HasRange(ABC):
    @abstractmethod
    def get_range(self):
        pass
