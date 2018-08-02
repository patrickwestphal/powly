from abc import ABC, abstractmethod
from itertools import chain

from powly.owl.model.hasoperands import HasOperands
from powly.owl.model.owlclassaxiom import OWLClassAxiom
from powly.owl.model.owlnaryaxiom import OWLNaryAxiom
from powly.owl.model.owlsubclassofaxiomsetshortcut import \
    OWLSubClassOfAxiomSetShortCut


class OWLNaryClassAxiom(
        OWLClassAxiom, OWLNaryAxiom, OWLSubClassOfAxiomSetShortCut,
        HasOperands, ABC):

    @abstractmethod
    def __init__(self, class_expressions, annotations):
        """
        :param class_expressions: A collection of OWLClassExpression objects
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(annotations)

        assert class_expressions is not None
        self.class_expressions = class_expressions
        self.class_expressions.sort()

    def components(self):
        return chain(
            (ce for ce in self.class_expressions),
            (ann for ann in self.annotations))

    def components_without_annotations(self):
        """TODO: Implement"""
        raise NotImplementedError()

    def components_annotations_first(self):
        """TODO: Implement"""
        raise NotImplementedError()

    def class_expressions(self):
        """
        Gets all of the top level class expressions that appear in this axiom.

        :return: Sorted stream of class expressions that appear in the axiom.
        """
        return (ce for ce in self.class_expressions)

    def operands(self):
        return self.class_expressions()

    def get_operands_as_list(self):
        return self.class_expressions

    def contains(self, ce):
        """
        Determines if this class axiom contains the specified class expression
        as an operand.

        :param ce: The OWLClassExpression object to test for
        :return: Boolean indicating whether the input class expression is
        contained in this axiom
        """
        return ce in self.class_expressions

    def get_class_expressions_minus(self, *ces):
        """
        Gets the set of class expressions that appear in this axiom minus the
        specfied class expressions.

        :param ces: The OWLClassExpression objects to subtract from the class
        expressions in this axiom
        :return: A set containing all of the OWLClassExpression objects in this
        axiom (the class expressions returned by getClassExpressions()) minus
        the specified list of class expressions
        """
        res = self.class_expressions[:]

        for ce in ces:
            try:
                while True:
                    res.remove(ce)
            except ValueError:
                pass

        return res
