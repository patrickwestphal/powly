from abc import abstractmethod, ABC

from powly.owl.model.swrlrulevisitorbase import SWRLRuleVisitorBase


class SWRLObjectVisitor(SWRLRuleVisitorBase, ABC):
    @abstractmethod
    def visit(self, node):
        """
        :param node: An object of one of the following classes:
        SWRLBuiltInAtom, SWRLClassAtom, SWRLDataPropertyAtom, SWRLDataRangeAtom,
        SWRLDifferentIndividualsAtom, SWRLIndividualArgument,
        SWRLLiteralArgument, SWRLObjectPropertyAtom, SWRLSameIndividualAtom,
        SWRLVariable; or one of these classes: SWRLRule
        """
        pass
