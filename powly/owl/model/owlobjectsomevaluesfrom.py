from rdflib.term import BNode

from powly.owl.model.classexpressiontype import ClassExpressionType
from powly.owl.model.owlclassexpressionvisitor import OWLClassExpressionVisitor
from powly.owl.model.owlclassexpressionvisitorex import \
    OWLClassExpressionVisitorEx
from powly.owl.model.owlobjectvisitor import OWLObjectVisitor
from powly.owl.model.owlobjectvisitorex import OWLObjectVisitorEx
from powly.owl.model.owlquantifiedobjectrestriction import \
    OWLQuantifiedObjectRestriction


class OWLObjectSomeValuesFrom(OWLQuantifiedObjectRestriction):
    """
    Represents an ObjectSomeValuesFrom class expression in the OWL 2
    Specification.
    """

    def __init__(self, property, filler):
        super().__init__(property, filler)
        self.property = property
        self.filler = filler
        self._cls_bnode = BNode()

    def __lt__(self, other):
        """
        TODO: Maybe do something more meaningful here
        """
        return str(self) < str(other)

    def get_class_expression_type(self):
        return ClassExpressionType.OBJECT_SOME_VALUES_FROM

    def accept(self, visitor):
        if isinstance(visitor, OWLClassExpressionVisitor) or \
                isinstance(visitor, OWLObjectVisitor):
            visitor.visit(self)

        elif isinstance(visitor, OWLClassExpressionVisitorEx) or \
                isinstance(visitor, OWLObjectVisitorEx):
            return visitor.visit(self)

        else:
            raise RuntimeError('Got wrong visitor type \'%s\'' % type(visitor))
