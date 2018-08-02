from abc import abstractmethod

from powly.owl.model.asowlnamedindividual import AsOWLNamedIndividual
from powly.owl.model.owlpropertyassertionobject import \
    OWLPropertyAssertionObject


class OWLIndividual(OWLPropertyAssertionObject, AsOWLNamedIndividual):
    """Represents a named or anonymous individual"""

    def is_named(self):
        """
        Determines if this individual is an instance of OWLNamedIndividual.
        Note that this method is the dual of is_anonymous().

        :return: A Boolean indicating whether this individual is an instance
        of OWLNamedIndividual
        """
        return self.is_owl_named_individual()

    @staticmethod
    def is_individual():
        return True

    @abstractmethod
    def as_owl_anonymous_individual(self):
        """
        Obtains this individual an anonymous individual if it is indeed
        anonymous.

        :return: An OWLAnonymousIndividual object,
        """
        pass

    @abstractmethod
    def to_string_id(self):
        pass

    def accept(self):
        raise NotImplementedError()
