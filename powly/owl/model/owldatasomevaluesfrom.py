from powly.owl.model.owlquantifieddatarestriction import \
    OWLQuantifiedDataRestriction


class OWLDataSomeValuesFrom(OWLQuantifiedDataRestriction):
    """
    Represents a
    <a href="http://www.w3.org/TR/owl2-syntax/#Existential_Quantification_2" >DataSomeValuesFrom</a>
    restriction in the OWL 2 Specification.
    """
    def __init__(self, property, filler):
        """
        :param property: An OWLDataPropertyExpression object
        :param filler: An OWLDataRange object
        """
        super().__init__(property, filler)

    def hash_index(self):
        return 181

    def type_index(self):
        return 3012

    def get_class_expression_type(self):
        from powly.owl.model.classexpressiontype import ClassExpressionType
        return ClassExpressionType.DATA_SOME_VALUES_FROM

    def accept(self, visitor):
        raise NotImplementedError()

