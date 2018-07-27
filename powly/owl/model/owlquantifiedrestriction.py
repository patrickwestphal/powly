from abc import abstractmethod, ABC

from powly.owl.model.owlrestriction import OWLRestriction


class OWLQuantifiedRestriction(OWLRestriction, ABC):
    @abstractmethod
    def __init__(self, filler):
        self.filler = filler

    def get_filler(self):
        return self.filler

    def components(self):
        raise NotImplementedError()
