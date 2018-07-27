from abc import abstractmethod, ABC

from powly.owl.model.owlclassvisitorbase import OWLClassVisitorBase
from powly.owl.model.owldataentityvisitorbase import OWLDataEntityVisitorBase
from powly.owl.model.owlindividualentityvisitorbase import OWLIndividualEntityVisitorBase
from powly.owl.model.owlpropertyentityvisitorbase import OWLPropertyEntityVisitorBase
from powly.owl.model.owlvisitorbase import OWLVisitorBase


class OWLEntityVisitor(
        OWLClassVisitorBase, OWLDataEntityVisitorBase,
        OWLIndividualEntityVisitorBase, OWLPropertyEntityVisitorBase,
        OWLVisitorBase, ABC):

    @abstractmethod
    def visit(self, entity):
        """
        :param entity: An object of one of these classes: OWLClass, OWLDatatype,
        OWLNamedIndividual, OWLAnnotationProperty, OWLDataProperty,
        OWLObjectProperty
        :return:
        """
        pass
