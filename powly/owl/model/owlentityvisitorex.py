from abc import abstractmethod, ABC

from powly.owl.model.owlclassvisitorexbase import OWLClassVisitorExBase
from powly.owl.model.owldataentityvisitorexbase import OWLDataEntityVisitorExBase
from powly.owl.model.owlindividualentityvisitorexbase import \
    OWLIndividualEntityVisitorExBase
from powly.owl.model.owlpropertyentityvisitorexbase import OWLPropertyEntityVisitorExBase
from powly.owl.model.owlvisitorexbase import OWLVisitorExBase


class OWLEntityVisitorEx(
        OWLClassVisitorExBase, OWLDataEntityVisitorExBase,
        OWLIndividualEntityVisitorExBase, OWLPropertyEntityVisitorExBase,
        OWLVisitorExBase, ABC):

    @abstractmethod
    def visit(self, entity):
        """
        :param entity: An object of one of these classes: OWLClass, OWLDatatype,
        OWLNamedIndividual, OWLAnnotationProperty, OWLDataProperty,
        OWLObjectProperty
        """
        pass
