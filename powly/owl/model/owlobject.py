from abc import ABC, abstractmethod

from powly.owl.util import compare_iterators
from powly.owl.model.hascomponent import HasComponents
from powly.owl.model.owlobjectvisitor import OWLObjectVisitor
from powly.owl.model.owlobjectvisitorex import OWLObjectVisitorEx


class OWLObject(HasComponents, ABC):
    @abstractmethod
    def type_index(self):
        pass

    @abstractmethod
    def hash_index(self):
        pass

    @staticmethod
    def nested_class_expressions():
        """
        Gets all of the nested (includes top level) class expressions that are
        used in this object.

        :return: A set of OWLClassExpression objects that represent the nested
        class expressions used in this object.
        """
        return set()

    def accept(self, visitor):
        """
        :param visitor: An object of one of the following classes:
        OWLObjectVisitor, OWLObjectVisitorEx
        """
        if isinstance(visitor, OWLObjectVisitor):
            visitor.visit(self)
        elif isinstance(visitor, OWLObjectVisitorEx):
            return visitor.visit(self)
        else:
            raise RuntimeError('Got wrong visitor type \'%s\'' % type(visitor))

    def is_top_entity(self):
        """
        Determines if this object is either, owl:Thing (the top class),
        owl:topObjectProperty (the top object property) , owl:topDataProperty
        (the top data property) or rdfs:Literal (the top datatype).

        :return: Boolean indicating whether this object corresponds to one of
        the above entities
        """
        return False

    def is_bottom_entity(self):
        """
        Determines if this object is either, owl:Nothing (the bottom class),
        owl:bottomObjectProperty (the bottom object property) ,
        owl:bottomDataProperty (the bottom data property).

        :return: Boolean indicating whether this object corresponds to one of
        the above entities
        """
        return False

    def is_iri(self):
        return False

    @staticmethod
    def is_individual():
        return False

    @staticmethod
    def is_axiom():
        return False

    @staticmethod
    def is_ontology():
        return False

    def is_anonymous_expression(self):
        return \
            (not self.is_axiom()) and \
            (not self.is_individual()) and \
            (not self.is_ontology()) and self.is_anonymous()

    def is_anonymous(self):
        """
        Actually part of the IsAnonymous interface
        """
        return False

    def has_shared_structure(self):
        """
        TODO: Implement

        :return: Boolean indicating whether this object contains anonymous
        expressions referred multiple times. This is called structure sharing.
        An example can be:
        <br>
        <pre>some P C subClassOf some Q (some P C)</pre>
        <br>

        This can happen in axioms as well as in expressions:
        <br>
        <pre>(some P C) and (some Q (some P C))</pre>
        <br>
        """
        counters = {}
        raise NotImplementedError()

    def anonymous_individuals(self):
        """
        TODO: implement

        :return: A stream of OWLAnonymousIndividual objects
        """
        raise NotImplementedError()

    def signature(self):
        """
        TODO: implement

        :return: A stream of OWLEntity objects
        """
        raise NotImplementedError()

    def contains_entity_in_signature(self, entity):
        """
        TODO: implement

        :return: Boolean indicating whether the input entity is contained in
        the OWLObject's signature
        """
        raise NotImplementedError()

    def classes_in_signature(self):
        """
        TODO: implement

        :return: A stream of OWLClass objects
        """
        raise NotImplementedError()

    def data_properties_in_signature(self):
        """
        TODO: implement

        :return: A stream of OWLDataProperty objects
        """
        raise NotImplementedError()

    def object_properties_in_signature(self):
        """
        TODO: Implement

        :return: A stream of OWLObjectProperty objects
        """
        raise NotImplementedError()

    def individuals_in_signature(self):
        """
        TODO: Implement

        :return: A stream of OWLNamedIndividual objects
        """
        raise NotImplementedError()

    def datatypes_in_signature(self):
        """
        TODO: Implement

        :return: A stream of OWLDatatype objects
        """
        raise NotImplementedError()

    def annotation_properties_in_signature(self):
        """
        TODO: Implement

        :return: A stream of OWLAnnotationProperty objects
        """
        raise NotImplementedError()

    def __eq__(self, other):
        if other == self:
            return True
        if other is None:
            return False
        if not isinstance(other, OWLObject):
            return False
        if hash(self) != hash(other):
            return False

        self_components = self.components()
        self_len = len(self_components)
        other_components = other.components()
        other_len = len(other_components)

        if self_len != other_len:
            return False
        else:
            for i in range(self_len):
                if self_components[i] != other_components[i]:
                    return False

            return True

    def compare_to(self, other):
        """
        :return: An integer value
        """
        assert other is not None
        if self.type_index() < other.type_index():
            diff = -1
            return diff
        elif self.type_index() == other.type_index():
            diff = 0
        else:
            diff = 1
            return diff

        return compare_iterators(self.components(), other.components())

    def __gt__(self, other):
        return self.compare_to(other) > 0

    def __lt__(self, other):
        return self.compare_to(other) < 0

    @staticmethod
    def hash_iteration(a, b):
        """
        :param a: An integer object
        :param b: An integer object
        :return: An integer object
        """
        return a * 37 + b
