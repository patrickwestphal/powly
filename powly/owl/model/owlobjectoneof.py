from powly.owl.model.classexpressiontype import ClassExpressionType
from powly.owl.model.hasoperands import HasOperands
from powly.owl.model.owlanonymousclassexpression import \
    OWLAnonymousClassExpression
from powly.owl.model.owlobject import OWLObject
from powly.owl.model.owlobjectunionof import OWLObjectUnionOf


class OWLObjectOneOf(OWLAnonymousClassExpression, HasOperands):
    """
    Represents an
    <a href="http://www.w3.org/TR/owl2-syntax/#Enumeration_of_Individuals" >ObjectOneOf</a>
    class expression in the OWL 2 Specification.
    """

    def __init__(self, values):
        """
        :param values: A collection/generator of OWLIndividual objects
        """
        super().__init__()
        assert values is not None
        self.values = values
        self.values.sort()

    def hash_index(self):
        return 229

    def type_index(self):
        return 3004

    def __hash__(self):
        return OWLObject.hash_iteration(
            self.hash_index(), hash(self.get_operands_as_list()))

    def components(self):
        return (op for op in self.get_operands_as_list())

    def get_class_expression_type(self):
        return ClassExpressionType.OBJECT_ONE_OF

    def individuals(self):
        """
        Gets the individuals that are in the oneOf. These individuals
        represent the exact instances (extension) of this class expression.
        """
        return (indiv for indiv in self.values)

    def get_operands_as_list(self):
        return self.values

    def operands(self):
        return self.individuals()

    def as_object_union_of(self):
        """
        Simplifies this enumeration to a union of singleton nominals.

        :return: This enumeration in a more standard DL form.
        simp({a}) = {a}
        simp({a0, ... , {an}) = unionOf({a0}, ... , {an})
        """
        if len(self.values) == 1:
            return self
        else:
            return OWLObjectUnionOf(
                map(lambda i: OWLObjectOneOf([i]), self.values))

    def accept(self, visitor):
        raise NotImplementedError()
