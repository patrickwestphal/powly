from abc import abstractmethod, ABC


class HasDomain(ABC):
    @abstractmethod
    def get_domain(self):
        pass
