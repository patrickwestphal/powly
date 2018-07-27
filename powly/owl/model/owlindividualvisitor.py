from abc import abstractmethod, ABC

from model.owlanonymousindividualvisitorbase import \
    OWLAnonymousIndividualVisitorBase
from model.owlindividualentityvisitorbase import OWLIndividualEntityVisitorBase
from model.owlvisitorbase import OWLVisitorBase


class OWLIndividualVisitor(
        OWLAnonymousIndividualVisitorBase, OWLIndividualEntityVisitorBase,
        OWLVisitorBase, ABC):

    @abstractmethod
    def visit(self, individual):
        """
        :param individual: Object of one of these classes:
        OWLAnonymousIndividual, OWLNamedIndividual
        """
        pass
