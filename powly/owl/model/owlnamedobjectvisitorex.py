from abc import abstractmethod, ABC

from powly.owl.model.owlentityvisitorex import OWLEntityVisitorEx
from powly.owl.model.owlindividualentityvisitorexbase import \
    OWLIndividualEntityVisitorExBase
from powly.owl.model.owlpropertyentityvisitorexbase import OWLPropertyEntityVisitorExBase


class OWLNamedObjectVisitorEx(
        OWLEntityVisitorEx, OWLIndividualEntityVisitorExBase,
        OWLPropertyEntityVisitorExBase, ABC):

    @abstractmethod
    def visit(self, entity):
        """
        :param entity: An object of one of the following classes: OWLOntology;
        or one of these: OWLClass, OWLDatatype, OWLNamedIndividual,
        OWLAnnotationProperty, OWLDataProperty, OWLObjectProperty
        """
        pass
