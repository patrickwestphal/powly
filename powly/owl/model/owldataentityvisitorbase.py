from abc import ABC, abstractmethod

from powly.owl.model.owlvisitorbase import OWLVisitorBase


class OWLDataEntityVisitorBase(OWLVisitorBase, ABC):
    @abstractmethod
    def visit(self, node):
        """
        :param node: An object of one of the following classes: OWLDatatype
        :return:
        """
        pass
