from abc import abstractmethod, ABC

from powly.owl.model.hasfiller import HasFiller
from powly.owl.model.owlrestriction import OWLRestriction


class OWLQuantifiedRestriction(OWLRestriction, HasFiller, ABC):
    @abstractmethod
    def __init__(self, filler):
        super().__init__()
        self.filler = filler

    def get_filler(self):
        return self.filler

    def components(self):
        raise NotImplementedError()
