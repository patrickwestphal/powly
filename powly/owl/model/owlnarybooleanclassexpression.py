from powly.owl.model.hasoperands import HasOperands
from powly.owl.model.owlbooleanclassexpression import OWLBooleanClassExpression


class OWLNaryBooleanClassExpression(OWLBooleanClassExpression, HasOperands):
    def __init__(self, operands):
        """
        :param operands: A collection/stream of OWLClassExpression objects
        """
        assert operands is not None
        self.operands = operands
        self.operands.sort()

    def components(self):
        """
        :return: A set of OWLClassExpression objects
        """
        raise NotImplementedError()

    def operands(self):
        """
        :return: A stream of OWLClassExpression objects
        """
        raise NotImplementedError()

    def get_operands_as_list(self):
        return self.operands
