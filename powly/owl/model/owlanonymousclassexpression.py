from abc import ABC

from powly.owl.model.owlclassexpression import OWLClassExpression


class OWLAnonymousClassExpression(OWLClassExpression, ABC):
    def as_conjunct_set(self):
        """
        TODO: Implement

        Interprets this expression as a conjunction and returns the conjuncts.

        :return: Set of OWLClassExpression objects
        """
        raise NotImplementedError()

    def conjunct_set(self):
        """TODO: Implement"""
        raise NotImplementedError()

    def as_disjunct_set(self):
        """
        TODO: Implement

        Interprets this expression as a disjunction and returns the disjuncts.

        :return: Set of OWLClassExpression objects
        """
        raise NotImplementedError()

    def disjunct_set(self):
        """TODO: Implement"""
        raise NotImplementedError()

    def contains_conjunct(self, ce):
        """
        Determines if this class expression contains a particular conjunct.

        :param ce: An OWLClassExpression object
        :return: Boolean
        """
        return ce == self

    def get_complement_nnf(self):
        """
        TODO: Implement

        Gets the negation normal form of the complement of this expression.

        :return: An OWLClassExpression object
        """
        raise NotImplementedError()

    def get_nnf(self):
        """
        TODO: Implement

        Gets this expression in negation normal form.

        :return: An OWLClassExpression object
        """
        raise NotImplementedError()

    def get_object_complement_of(self):
        """
        TODO: Implement

        Gets the object complement of this class expression.

        :return: An OWLClassExpression object
        """
        raise NotImplementedError()

    @staticmethod
    def is_anonymous():
        """
        Determines whether or not this expression represents an anonymous class
        expression.

        :return: A boolean indicating whether this expression is an anonymous
        class expression
        """
        return True

    @staticmethod
    def is_owl_nothing():
        """
        Determines if this expression is the built in class owl:Nothing.

        :return: A boolean indicating whether this expression is owl:Nothing
        """
        return False

    @staticmethod
    def is_owl_thing():
        """
        Determines if this expression is the built in class owl:Thing.

        :return: A boolean indicating whether this expression is owl:Thing
        """
        return False
