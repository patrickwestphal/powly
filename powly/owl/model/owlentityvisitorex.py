from abc import abstractmethod, ABC

from model.owlclassvisitorexbase import OWLClassVisitorExBase
from model.owldataentityvisitorexbase import OWLDataEntityVisitorExBase
from model.owlindividualentityvisitorexbase import \
    OWLIndividualEntityVisitorExBase
from model.owlpropertyentityvisitorexbase import OWLPropertyEntityVisitorExBase
from model.owlvisitorexbase import OWLVisitorExBase


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
