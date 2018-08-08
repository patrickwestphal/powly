from abc import abstractmethod, ABC

from powly.owl.model.owlobjectrestriction import OWLObjectRestriction
from powly.owl.model.owlquantifiedrestriction import OWLQuantifiedRestriction


class OWLQuantifiedObjectRestriction(
        OWLQuantifiedRestriction, OWLObjectRestriction, ABC):
    @abstractmethod
    def __init__(self, property, filler):
        """
        :param property: An OWLObjectPropertyExpression object
        :param filler: An OWLClassExpression object
        """
        super().__init__(filler)
        assert property is not None
        self.property = property

    def add_anonymous_individuals_to_set(self, anons):
        """
        :param anons: A set of OWLAnonymousIndividual objects
        """
        raise NotImplementedError()

    def add_signature_entities_to_set(self, entities):
        """
        :param entities: A set of OWLEntity objects
        """
        raise NotImplementedError()

    def get_property(self):
        """
        :return: An OWLObjectPropertyExpression object
        """
        return self.property
