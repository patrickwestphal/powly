from abc import abstractmethod, ABC

from model.owlvisitorbase import OWLVisitorBase


class OWLIndividualEntityVisitorBase(OWLVisitorBase, ABC):
    @abstractmethod
    def visit(self, individual):
        """
        :param individual: On object of one of the following classes:
        OWLNamedIndividual
        """
        pass
