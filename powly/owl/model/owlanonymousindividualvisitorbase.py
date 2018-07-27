from abc import ABC, abstractmethod

from model.owlvisitorbase import OWLVisitorBase


class OWLAnonymousIndividualVisitorBase(OWLVisitorBase, ABC):
    @abstractmethod
    def visit(self, individual):
        """
        :param individual: An object of one of the following classes:
        OWLAnonymousIndividual
        """
        pass
