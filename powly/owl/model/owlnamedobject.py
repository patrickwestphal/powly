from abc import abstractmethod, ABC

from powly.owl.model.hasiri import HasIRI
from powly.owl.model.owlnamedobjectvisitor import OWLNamedObjectVisitor
from powly.owl.model.owlnamedobjectvisitorex import OWLNamedObjectVisitorEx
from powly.owl.model.owlobject import OWLObject


class OWLNamedObject(OWLObject, HasIRI, ABC):
    """
    Represents a named object for example, class, property, ontology etc. - i.e.
    anything that has an IRI as its name.
    """

    @abstractmethod
    def accept(self, visitor):
        """
        :param visitor: An object of one of the following classes:
        OWLNamedObjectVisitor, OWLNamedObjectVisitorEx; or one of these classes
        OWLObjectVisitor, OWLObjectVisitorEx
        """
        pass
