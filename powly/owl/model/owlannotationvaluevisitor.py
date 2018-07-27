from abc import ABC, abstractmethod

from powly.owl.model.owlanonymousindividualvisitorbase import \
    OWLAnonymousIndividualVisitorBase
from powly.owl.model.owlliteralvisitorbase import OWLLiteralVisitorBase
from powly.owl.model.owlvisitorbase import OWLVisitorBase


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
