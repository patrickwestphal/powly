from powly.owl.model.owlobjectcardinalityrestriction import \
    OWLObjectCardinalityRestriction


class OWLObjectMinCardinality(OWLObjectCardinalityRestriction):
    """
    Represents a
    <a href="http://www.w3.org/TR/owl2-syntax/#Minimum_Cardinality">ObjectMinCardinality</a>
    restriction in the OWL 2 Specification.
    """

    def __init__(self, property, cardinality, filler):
        """
        :param property: An OWLObjectPropertyExpression object
        :param cardinality: An integer object
        :param filler: An OWLClassExpression object
        """
        super().__init__(property, cardinality, filler)

    def hash_index(self):
        return 227

    def type_index(self):
        return 3008

    def get_class_expression_type(self):
        from powly.owl.model.classexpressiontype import ClassExpressionType
        return ClassExpressionType.OBJECT_MIN_CARDINALITY

    def accept(self, visitor):
        raise NotImplementedError()
