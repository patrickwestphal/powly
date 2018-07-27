from abc import abstractmethod, ABC

from powly.owl.model.owlvisitorexbase import OWLVisitorExBase


class OWLAnonymousIndividualVisitorExBase(OWLVisitorExBase, ABC):
    @abstractmethod
    def visit(self, individual):
        """
        :param individual: An object of one of the following classes:
        OWLAnonymousIndividual
        """
        pass
