from abc import ABC, abstractmethod


class HasCardinality(ABC):
    @abstractmethod
    def get_cardinality(self):
        """
        :return: An integer object
        """
        pass
