from powly.owl.model.owlcardinalityrestriction import OWLCardinalityRestriction
from powly.owl.model.owlobjectrestriction import OWLObjectRestriction
from powly.owl.model.owlquantifiedobjectrestriction import \
    OWLQuantifiedObjectRestriction


class OWLObjectCardinalityRestriction(
        OWLCardinalityRestriction, #OWLQuantifiedObjectRestriction,
        OWLObjectRestriction):
    def __init__(self, property, cardinality, filler):
        """
        :param property: An OWLObjectPropertyExpression object
        :param cardinality: An integer object
        :param filler: An OWLClassExpression object
        """
        super().__init__(cardinality, filler)
        assert property is not None
        self.property = property

    def get_property(self):
        return self.property
