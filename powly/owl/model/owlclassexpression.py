from abc import abstractmethod, ABC

from model.asowlclass import AsOWLClass
from model.owlpropertyrange import OWLPropertyRange
from model.swrlpredicate import SWRLPredicate


class OWLClassExpression(OWLPropertyRange, SWRLPredicate, AsOWLClass, ABC):
    """
    Represents Class Expressions in the OWL 2 specification. This covers named
    and anonymous classes.
    """

    @abstractmethod
    def accept(self, visitor):
        """
        :param visitor: An object of one of the following types:
        OWLClassExpressionVisitor, OWLClassExpressionVisitorEx
        """
        pass

    @abstractmethod
    def as_conjunct_set(self):
        """
        Interprets this expression as a conjunction and returns the conjuncts.

        :return: A set of OWLClassExpression objects
        """
        pass

    @abstractmethod
    def as_disjunct_set(self):
        """
        Interprets this expression as a disjunction and returns the disjuncts.

        :return: A set of OWLClassExpression objects
        """
        pass

    def conjunct_set(self):
        """
        Interprets this expression as a conjunction and returns the conjuncts.
        """
        raise NotImplementedError()

    @abstractmethod
    def contains_conjunct(self, ce):
        """
        Determines if this class expression contains a particular conjunct.

        :param ce: An OWLClassExpression object
        :return: Boolean indicating whether this expression contains the input
        class expression as conjunct
        """
        pass

    def disjunct_set(self):
        """
        Interprets this expression as a disjunction and returns the disjuncts.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_class_expression_type(self):
        """
        Gets the class expression type for this class expression.

        :return: A ClassExpressionType object
        """
        pass

    @abstractmethod
    def get_complement_nnf(self):
        """
        Gets the negation normal form of the complement of this expression.

        :return: An OWLClassExpression object
        """
        pass

    @abstractmethod
    def get_nnf(self):
        """
        Gets this expression in negation normal form.

        :return: An OWLClassExpression object
        """
        pass

    @abstractmethod
    def get_object_complement_of(self):
        """
        Gets the object complement of this class expression.

        :return: An OWLClassExpression object
        """
        pass

    def is_class_expression_literal(self):
        """
        Determines if this class is a literal.

        :return: Boolean indicating whether this class is a class literal
        """
        return False

    @abstractmethod
    def is_owl_nothing(self):
        """
        Determines if this expression is the built in class owl:Nothing.

        :return: Boolean indicating whether this expression is the built in
        class owl:Nothing
        """
        pass

    @abstractmethod
    def is_owl_thing(self):
        """
        Determines if this expression is the built in class owl:Thing.

        :return: Boolean indicating whether this expression is the built in
        class owl:Thing
        """
        pass
