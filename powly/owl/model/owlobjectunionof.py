from powly.owl.model.owlnarybooleanclassexpression import \
    OWLNaryBooleanClassExpression


class OWLObjectUnionOf(OWLNaryBooleanClassExpression):
    def __init__(self, operands):
        """
        :param operands: A generator for or list of OWLClassExpression objects
        """
        super().__init__(operands)

    def as_disjunct_set(self):
        raise NotImplementedError()

    def disjunct_set(self):
        raise NotImplementedError()

    def get_class_expression_type(self):
        """
        TODO: Implement

        :return: An ClassExpressionType object
        """
        raise NotImplementedError()

    def accept(self, visitor):
        """
        TODO: Implement

        :param visitor:
        """
        raise NotImplementedError()
