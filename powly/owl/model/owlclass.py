from rdflib.term import URIRef

from powly.owl.model.classexpressiontype import ClassExpressionType
from powly.owl.model.entitytype import EntityType
from powly.owl.model.owlclassexpression import OWLClassExpression
from powly.owl.model.owlclassexpressionvisitor import OWLClassExpressionVisitor
from powly.owl.model.owlclassexpressionvisitorex import OWLClassExpressionVisitorEx
from powly.owl.model.owlentityvisitor import OWLEntityVisitor
from powly.owl.model.owlentityvisitorex import OWLEntityVisitorEx
from powly.owl.model.owllogicalentity import OWLLogicalEntity
from powly.owl.model.owlnamedobject import OWLNamedObject
from powly.owl.model.owlnamedobjectvisitor import OWLNamedObjectVisitor
from powly.owl.model.owlnamedobjectvisitorex import OWLNamedObjectVisitorEx
from powly.owl.model.owlobjectvisitor import OWLObjectVisitor
from powly.owl.model.owlobjectvisitorex import OWLObjectVisitorEx


class OWLClass(OWLClassExpression, OWLLogicalEntity, OWLNamedObject):
    """
    Represents a Class in the OWL 2 specification.
    """

    def __init__(self, uri_or_str):
        super().__init__()
        if isinstance(uri_or_str, str):
            self.iri = URIRef(uri_or_str)
        elif isinstance(uri_or_str, URIRef):
            self.iri = uri_or_str
        else:
            raise RuntimeError('Unknown type for %s (%s)' % (
                str(uri_or_str), type(uri_or_str)))

    def __lt__(self, other):
        """
        TODO: Also consider annotations here
        """
        return str(self.iri) < str(other.iri)

    def components(self):
        return (c for c in [self.iri])

    def accept(self, visitor):
        """
        :param visitor: An object of one of the following classes:
        OWLClassExpressionVisitor, OWLClassExpressionVisitorEx,
        OWLEntityVisitor, OWLEntityVisitorEx, OWLNamedObjectVisitor,
        OWLNamedObjectVisitorEx, OWLObjectVisitor, OWLObjectVisitorEx
        """
        if isinstance(visitor, OWLClassExpressionVisitor) or \
                isinstance(visitor, OWLEntityVisitor) or \
                isinstance(visitor, OWLNamedObjectVisitor) or \
                isinstance(visitor, OWLObjectVisitor):
            visitor.visit(self)

        elif isinstance(visitor, OWLClassExpressionVisitorEx) or \
                isinstance(visitor, OWLEntityVisitorEx) or \
                isinstance(visitor, OWLNamedObjectVisitorEx) or \
                isinstance(visitor, OWLObjectVisitorEx):
            return visitor.visit(self)

        else:
            raise RuntimeError('Got wrong visitor type \'%s\'' % type(visitor))

    def get_class_expression_type(self):
        """
        Gets the class expression type for this class expression.

        :return: A ClassExpressionType object
        """
        return ClassExpressionType.OWL_CLASS

    @staticmethod
    def get_entity_type():
        """
        Gets the entity type for this entity.

        :return: An EntityType object
        """
        return EntityType.CLASS

    def is_bottom_entity(self):
        """
        Determines if this object is either, owl:Nothing (the bottom class),
        owl:bottomObjectProperty (the bottom object property) ,
        owl:bottomDataProperty (the bottom data property).

        :return: Boolean
        """
        return self.is_owl_nothing()

    @staticmethod
    def is_owl_class():
        """
        A convenience method that determines if this entity is an OWLClass.

        :return: Boolean
        """
        return True

    def is_top_entity(self):
        """
        Determines if this object is either, owl:Thing (the top class),
        owl:topObjectProperty (the top object property) , owl:topDataProperty
        (the top data property) or rdfs:Literal (the top datatype).

        :return: Boolean
        """
        return self.is_owl_thing()

    def as_conjunct_set(self):
        """
        Interprets this expression as a conjunction and returns the conjuncts.

        :return: A set of OWLClassExpression objects
        """
        raise NotImplementedError()

    def as_disjunct_set(self):
        """
        Interprets this expression as a disjunction and returns the disjuncts.

        :return: A set of OWLClassExpression objects
        """
        raise NotImplementedError()

    def conjunct_set(self):
        """
        Interprets this expression as a conjunction and returns the conjuncts.

        :return: A stream of OWLClassExpression objects
        """
        raise NotImplementedError()

    def contains_conjunct(self, ce):
        """
        Determines if this class expression contains a particular conjunct.

        :param ce: An OWLClassExpression object
        :return: Boolean determining whether this class expression contains the
        input class expression as conjunct
        """
        raise NotImplementedError()

    def disjunct_set(self):
        """
        Interprets this expression as a disjunction and returns the disjuncts.

        :return: A stream of OWLClassExpression objects
        """
        raise NotImplementedError()

    def get_complement_nnf(self):
        """
        Gets the negation normal form of the complement of this expression.

        :return: An OWLClassExpression object
        """
        raise NotImplementedError()

    def get_nnf(self):
        """
        Gets this expression in negation normal form.

        :return: An OWLClassExpression object
        """
        raise NotImplementedError()

    def get_object_complement_of(self):
        """
        Gets the object complement of this class expression.

        :return: An OWLClassExpression object
        """
        raise NotImplementedError()

    def is_built_in(self):
        """
        Determines if this entity is a built in entity.

        :return: Boolean determining whether this entity is a built in entity
        """
        raise NotImplementedError()

    def is_owl_nothing(self):
        """
        Determines if this expression is the built in class owl:Nothing.

        :return: Boolean determining whether this expression is owl:Nothing
        """
        raise NotImplementedError()

    def is_owl_thing(self):
        """
        Determines if this expression is the built in class owl:Thing.

        :return: Boolean determining whether this expression is owl:Thing
        """
        raise NotImplementedError()

    def is_class_expression_literal(self):
        return True

    def to_string_id(self):
        return str(self.iri)

    def get_iri(self):
        return self.iri
