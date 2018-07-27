from abc import abstractmethod, ABC

from powly.owl.model.owlanonymousindividualvisitorbase import \
    OWLAnonymousIndividualVisitorBase
from powly.owl.model.owlindividualentityvisitorbase import OWLIndividualEntityVisitorBase
from powly.owl.model.owlvisitorbase import OWLVisitorBase


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
