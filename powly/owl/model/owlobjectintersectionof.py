from powly.owl.model.owlnarybooleanclassexpression import \
    OWLNaryBooleanClassExpression


class OWLObjectIntersectionOf(OWLNaryBooleanClassExpression):
    """
    Represents an
    <a href="http://www.w3.org/TR/owl2-syntax/#Intersection_of_Class_Expressions">ObjectIntersectionOf</a>
    class expression in the OWL 2 Specification.
    """

    def __init__(self, operands):
        """
        :param operands: A collection/stream of OWLClassExpression objects
        """
        super().__init__(operands)

    def hash_index(self):
        return 211

    def type_index(self):
        return 3001

    def as_conjunct_set(self):
        """TODO: Implement"""
        raise NotImplementedError()

    def conjunct_set(self):
        """TODO: Implement"""
        raise NotImplementedError()

    def contains_conjunct(self, ce):
        """TODO: Implement"""
        raise NotImplementedError()

    def get_class_expression_type(self):
        """TODO: Implement"""
        raise NotImplementedError()

    def accept(self, visitor):
        """TODO: Implement"""
        raise NotImplementedError()
