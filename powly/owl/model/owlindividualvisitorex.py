from abc import abstractmethod, ABC

from model.owlanonymousindividualvisitorexbase import \
    OWLAnonymousIndividualVisitorExBase
from model.owlindividualentityvisitorexbase import \
    OWLIndividualEntityVisitorExBase
from model.owlvisitorexbase import OWLVisitorExBase


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
