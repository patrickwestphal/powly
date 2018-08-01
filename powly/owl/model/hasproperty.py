from abc import ABC, abstractmethod


class HasProperty(ABC):
    @abstractmethod
    def get_property(self):
        pass
