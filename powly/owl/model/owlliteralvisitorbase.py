from abc import abstractmethod, ABC

from model.owlvisitorbase import OWLVisitorBase


class OWLLiteralVisitorBase(OWLVisitorBase, ABC):
    @abstractmethod
    def visit(self, node):
        """
        :param node: An object of one of the following classes: OWLLiteral
        """
        pass
