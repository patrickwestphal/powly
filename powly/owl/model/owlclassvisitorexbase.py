from abc import abstractmethod, ABC

from model.owlvisitorexbase import OWLVisitorExBase


class OWLClassVisitorExBase(OWLVisitorExBase, ABC):
    """
    An interface to objects that can visit OWLClassExpressions.
    """

    @abstractmethod
    def visit(self, ce):
        """
        :param ce: An object of one of the following classes: OWLClass
        """
        pass
