from abc import abstractmethod, ABC

from model.owlnamedobjectvisitor import OWLNamedObjectVisitor
from model.owlnamedobjectvisitorex import OWLNamedObjectVisitorEx
from model.owlobject import OWLObject


class OWLNamedObject(OWLObject, ABC):
    """
    Represents a named object for example, class, property, ontology etc. - i.e.
    anything that has an IRI as its name.
    """

    @abstractmethod
    def __init__(self, *args):
        pass

    def accept(self, visitor):
        """
        :param visitor: An object of one of the following classes:
        OWLNamedObjectVisitor, OWLNamedObjectVisitorEx; or one of these classes
        OWLObjectVisitor, OWLObjectVisitorEx
        """
        if isinstance(visitor, OWLNamedObjectVisitor):
            visitor.visit(self)
        elif isinstance(visitor, OWLNamedObjectVisitorEx):
            return visitor.visit(self)
        else:
            return super().accept(visitor)
