from powly.owl.model.owllogicalentity import OWLLogicalEntity
from powly.owl.model.owlpropertyexpression import OWLPropertyExpression


class OWLProperty(OWLPropertyExpression, OWLLogicalEntity):
    """
    A marker interface for properties that aren't expression i.e. named
    properties. By definition, properties are either data properties or object
    properties.
    """
