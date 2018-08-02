from abc import abstractmethod, ABC


class HasIRI(ABC):
    @abstractmethod
    def get_iri(self):
        pass
