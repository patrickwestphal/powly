from abc import ABC, abstractmethod

from model.owlvisitorbase import OWLVisitorBase


class OWLClassVisitorBase(OWLVisitorBase, ABC):
    """
    An interface to objects that can visit OWLClassExpressions. (See the
    Visitor Patterns)
    """

    @abstractmethod
    def visit(self, ce):
        """
        :param ce: An OWLClass object to visit
        :return:
        """
        pass
