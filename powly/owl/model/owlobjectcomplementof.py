from powly.owl.model.owlbooleanclassexpression import OWLBooleanClassExpression
from powly.owl.model.owlobject import OWLObject


class OWLObjectComplementOf(OWLBooleanClassExpression):

    def __init__(self, operand):
        """
        :param operand: An OWLClassExpression object
        """
        super().__init__()
        assert operand is not None
        self.operand = operand

    def hash_index(self):
        return 197

    def type_index(self):
        return 3003

    def __hash__(self):
        hsh = self.hash_index()
        return OWLObject.hash_iteration(hsh, hash(self.get_operand()))

    def is_class_expression_literal(self):
        return not self.operand.is_anonymous()

    def components(self):
        return (o for o in [self.get_operand()])

    def get_class_expression_type(self):
        from powly.owl.model.classexpressiontype import ClassExpressionType
        return ClassExpressionType.OBJECT_COMPLEMENT_OF

    def get_operand(self):
        return self.operand

    def accept(self, visitor):
        raise NotImplementedError()

