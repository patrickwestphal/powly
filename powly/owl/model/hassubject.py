from abc import ABC, abstractmethod


class HasSubject(ABC):
    @abstractmethod
    def get_subject(self):
        pass
