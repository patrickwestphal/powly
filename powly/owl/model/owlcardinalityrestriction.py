import itertools

from powly.owl.model.hascardinality import HasCardinality
from powly.owl.model.owlobject import OWLObject
from powly.owl.model.owlquantifiedrestriction import OWLQuantifiedRestriction


class OWLCardinalityRestriction(OWLQuantifiedRestriction, HasCardinality):

    def __init__(self, cardinality, filler):
        """
        :param cardinality: An integer object
        :param filler: An OWLPropertyRange object
        """
        super().__init__(filler)
        assert cardinality is not None
        self.cardinality = cardinality

    def __hash__(self):
        hsh = self.hash_index()
        hsh = OWLObject.hash_iteration(hsh, hash(self.get_property()))
        hsh = OWLObject.hash_iteration(hsh, hash(self.get_cardinality()))
        return OWLObject.hash_iteration(hsh, hash(self.get_filler()))

    def components(self):
        return itertools.chain(
            (p for p in [self.get_property()]),
            (i for i in [self.get_cardinality()]),
            (f for f in [self.get_filler()]))

    def is_qualified(self):
        """
        Determines if this restriction is qualified. Qualified cardinality
        restrictions are defined to be cardinality restrictions that have
        fillers which aren't TOP (owl:Thing or rdfs:Literal). An object
        restriction is unqualified if it has a filler that is owl:Thing. A data
        restriction is unqualified if it has a filler which is the top data
        type (rdfs:Literal).
        :return:
        """
        return not self.get_filler().is_top_entity()

    def get_cardinality(self):
        return self.cardinality

    def get_filler(self):
        return self.filler
