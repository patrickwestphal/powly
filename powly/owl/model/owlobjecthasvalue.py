from powly.owl.model.classexpressiontype import ClassExpressionType
from powly.owl.model.owlhasvaluerestriction import OWLHasValueRestriction
from powly.owl.model.owlobjectoneof import OWLObjectOneOf
from powly.owl.model.owlobjectrestriction import OWLObjectRestriction
from powly.owl.model.owlobjectsomevaluesfrom import OWLObjectSomeValuesFrom


class OWLObjectHasValue(OWLHasValueRestriction, OWLObjectRestriction):
    """
    Represents an
    <a href="http://www.w3.org/TR/owl2-syntax/#Individual_Value_Restriction" >ObjectHasValue</a>
    class expression in the OWL 2 Specification.
    """

    def __init__(self, property, value):
        """
        :param property: An OWLObjectProperty object
        :param value: An OWLIndividual object
        """
        super().__init__(value)
        assert property is not None
        self.property = property

    def hash_index(self):
        return 251

    def type_index(self):
        return 3007

    def get_property(self):
        return self.property

    def get_class_expression_type(self):
        return ClassExpressionType.OBJECT_HAS_VALUE

    def accept(self, visitor):
        raise NotImplementedError()

    def as_some_values_from(self):
        return OWLObjectSomeValuesFrom(
            self.property, OWLObjectOneOf(self.get_filler()))
