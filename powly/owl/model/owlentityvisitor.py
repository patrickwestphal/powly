from abc import abstractmethod, ABC

from model.owlclassvisitorbase import OWLClassVisitorBase
from model.owldataentityvisitorbase import OWLDataEntityVisitorBase
from model.owlindividualentityvisitorbase import OWLIndividualEntityVisitorBase
from model.owlpropertyentityvisitorbase import OWLPropertyEntityVisitorBase
from model.owlvisitorbase import OWLVisitorBase


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
