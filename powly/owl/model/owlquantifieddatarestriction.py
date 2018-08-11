from abc import abstractmethod

from powly.owl.model.owldatarestriction import OWLDataRestriction
from powly.owl.model.owlquantifiedrestriction import OWLQuantifiedRestriction


class OWLQuantifiedDataRestriction(
        OWLQuantifiedRestriction, OWLDataRestriction):
    @abstractmethod
    def __init__(self, property, filler):
        """
        :param property: An OWLDataPropertyExpression object
        :param filler: An OWLDataRange object
        """
        super().__init__(filler)
        assert property is not None
        self.property = property

    def get_property(self):
        return self.property
