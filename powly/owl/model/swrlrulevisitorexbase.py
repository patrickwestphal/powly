from abc import abstractmethod, ABC

from powly.owl.model.owlvisitorexbase import OWLVisitorExBase


class SWRLRuleVisitorExBase(OWLVisitorExBase, ABC):
    @abstractmethod
    def visit(self, node):
        """
        :param node: An object of one of the following classes: SWRLRule
        """
        pass
