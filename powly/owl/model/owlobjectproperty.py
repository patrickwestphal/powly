from rdflib.term import URIRef

from powly.owl.model.entitytype import EntityType
from powly.owl.model.owlentityvisitor import OWLEntityVisitor
from powly.owl.model.owlentityvisitorex import OWLEntityVisitorEx
from powly.owl.model.owlnamedobjectvisitor import OWLNamedObjectVisitor
from powly.owl.model.owlnamedobjectvisitorex import OWLNamedObjectVisitorEx
from powly.owl.model.owlobjectpropertyexpression import \
    OWLObjectPropertyExpression
from powly.owl.model.owlobjectvisitor import OWLObjectVisitor
from powly.owl.model.owlobjectvisitorex import OWLObjectVisitorEx
from powly.owl.model.owlproperty import OWLProperty
from powly.owl.model.owlpropertyexpressionvisitor import \
    OWLPropertyExpressionVisitor
from powly.owl.model.owlpropertyexpressionvisitorex import \
    OWLPropertyExpressionVisitorEx
from powly.owl.vocab.owlrdfvocabulary import OWLRDFVocabulary


class OWLObjectProperty(OWLObjectPropertyExpression, OWLProperty):
    """
    Represents an
    <a href="http://www.w3.org/TR/owl2-syntax/#Object_Properties">Object Property</a>
    in the OWL 2 Specification.
    """
    def __init__(self, iri_or_str):
        super().__init__()
        if isinstance(iri_or_str, str):
            self.iri = URIRef(iri_or_str)
        else:
            self.iri = iri_or_str
        self.built_in = self.iri in {
            OWLRDFVocabulary.OWL_TOP_OBJECT_PROPERTY.iri,
            OWLRDFVocabulary.OWL_BOTTOM_OBJECT_PROPERTY.iri}

    def __gt__(self, other):
        """
        TODO: Also consider annotations here
        """
        return str(self.iri) > str(other.iri)

    def get_entity_type(self):
        return EntityType.OBJECT_PROPERTY

    def get_named_property(self):
        return self

    @staticmethod
    def is_owl_object_property():
        return True

    def is_top_entity(self):
        return self.is_owl_top_object_property()

    def is_bottom_entity(self):
        return self.is_owl_bottom_object_property()

    def is_owl_top_object_property(self):
        return self.iri == OWLRDFVocabulary.OWL_TOP_OBJECT_PROPERTY.iri

    def is_owl_bottom_object_property(self):
        return self.iri == OWLRDFVocabulary.OWL_BOTTOM_OBJECT_PROPERTY.iri

    def accept(self, visior):
        """
        :param visior: An object of one of the following classes:
        OWLObjectVisitor, OWLObjectVisitorEx, OWLPropertyExpressionVisitor,
        OWLPropertyExpressionVisitorEx, OWLEntityVisitor, OWLEntityVisitorEx,
        OWLNamedObjectVisitor, OWLNamedObjectVisitorEx; or one of these classes:
        OWLEntityVisitor, OWLNamedObjectVisitor, OWLNamedObjectVisitorEx,
        OWLObjectVisitor, OWLObjectVisitorEx, OWLPropertyExpressionVisitor,
        OWLPropertyExpressionVisitorEx
        """
        if isinstance(visior, OWLObjectVisitor) or \
                isinstance(visior, OWLPropertyExpressionVisitor) or \
                isinstance(visior, OWLEntityVisitor) or \
                isinstance(visior, OWLNamedObjectVisitor):
            visior.visit(self)
        elif isinstance(visior, OWLObjectVisitorEx) or \
                isinstance(visior, OWLPropertyExpressionVisitorEx) or \
                isinstance(visior, OWLEntityVisitorEx) or \
                isinstance(visior, OWLNamedObjectVisitorEx):
            return visior.visit(self)
        else:
            super().accept(visior)

    def to_string_id(self):
        return str(self.iri)

    def is_built_in(self):
        return self.built_in

    def get_inverse_property(self):
        """
        TODO: Implement
        :return: An OWLObjectInverseOf object
        """
        raise NotImplementedError()

    def components(self):
        return (c for c in [self.iri])

    def get_iri(self):
        return self.iri
