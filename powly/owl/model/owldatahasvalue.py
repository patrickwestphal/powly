from powly.owl.model.owldatarestriction import OWLDataRestriction
from powly.owl.model.owlhasvaluerestriction import OWLHasValueRestriction


class OWLDataHasValue(OWLHasValueRestriction, OWLDataRestriction):
    """
    Represents
    <a href="http://www.w3.org/TR/owl2-syntax/#Literal_Value_Restriction">DataHasValue</a>
    restrictions in the OWL 2 Specification.
    """
    def __init__(self, property, value):
        """
        :param property: An OWLDataPropertyExpression object
        :param value: An OWLLiteral object
        """
        super().__init__(value)
        assert property is not None
        self.property = property

    def hash_index(self):
        return 191

    def type_index(self):
        return 3014

    def get_class_expression_type(self):
        from powly.owl.model.classexpressiontype import ClassExpressionType
        return ClassExpressionType.DATA_HAS_VALUE

    def get_property(self):
        return self.property

    def as_some_values_from(self):
        # return OWLDataSomeValuesFrom(self.property, OWLDataOneOf(self.filler))
        raise NotImplementedError()

    def accept(self, visitor):
        raise NotImplementedError()
