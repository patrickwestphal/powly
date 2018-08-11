from powly.owl.model.owlobjectcardinalityrestriction import \
    OWLObjectCardinalityRestriction


class OWLObjectExactCardinality(OWLObjectCardinalityRestriction):
    """
    Represents an
    <a href="http://www.w3.org/TR/owl2-syntax/#Exact_Cardinality">ObjectExactCardinality</a>
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
        return 199

    def type_index(self):
        return 3009

    def get_class_expression_type(self):
        from powly.owl.model.classexpressiontype import ClassExpressionType
        return ClassExpressionType.OBJECT_EXACT_CARDINALITY

    def as_intersection_of_min_max(self):
        raise NotImplementedError()

    def accept(self, visitor):
        raise NotImplementedError()
