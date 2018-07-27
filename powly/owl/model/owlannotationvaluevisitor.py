from abc import ABC, abstractmethod

from model.owlanonymousindividualvisitorbase import \
    OWLAnonymousIndividualVisitorBase
from model.owlliteralvisitorbase import OWLLiteralVisitorBase
from model.owlvisitorbase import OWLVisitorBase


class OWLAnnotationValueVisitor(
        OWLAnonymousIndividualVisitorBase, OWLLiteralVisitorBase,
        OWLVisitorBase, ABC):

    @abstractmethod
    def visit(self, entity):
        """
        :param entity: An object of one of the following classes: IRI; or one of
        these classes: OWLAnonymousIndividual, OWLLiteral
        """
        pass
