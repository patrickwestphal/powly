from abc import abstractmethod, ABC

from powly.owl.model.owlanonymousindividualvisitorexbase import \
    OWLAnonymousIndividualVisitorExBase
from powly.owl.model.owlliteralvisitorexbase import OWLLiteralVisitorExBase
from powly.owl.model.owlvisitorexbase import OWLVisitorExBase


class OWLAnnotationValueVisitorEx(
        OWLAnonymousIndividualVisitorExBase, OWLLiteralVisitorExBase,
        OWLVisitorExBase, ABC):

    @abstractmethod
    def visit(self, entity):
        """
        :param entity: An object of one of the following classes: IRI; or of
        these classes: OWLAnonymousIndividual, OWLLiteral
        """
        pass
