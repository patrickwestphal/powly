from abc import abstractmethod, ABC

from powly.owl.model.owlanonymousindividualvisitorexbase import \
    OWLAnonymousIndividualVisitorExBase
from powly.owl.model.owlindividualentityvisitorexbase import \
    OWLIndividualEntityVisitorExBase
from powly.owl.model.owlvisitorexbase import OWLVisitorExBase


class OWLIndividualVisitorEx(
        OWLAnonymousIndividualVisitorExBase, OWLIndividualEntityVisitorExBase,
        OWLVisitorExBase, ABC):

    @abstractmethod
    def visit(self, individual):
        """
        :param individual: An object of one of these classes:
        OWLAnonymousIndividual, OWLNamedIndividual
        """
        pass
