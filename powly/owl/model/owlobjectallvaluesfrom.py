from powly.owl.model.owlquantifiedobjectrestriction import \
    OWLQuantifiedObjectRestriction


class OWLObjectAllValuesFrom(OWLQuantifiedObjectRestriction):
    def __init__(self, property, filler):
        """
        :param property_expression: An OWLObjectPropertyExpression object
        :param filler: An OWLClassExpression object
        """
        super().__init__(property, filler)

    def get_class_expression_type(self):
        """
        TODO: Implement
        """
        raise NotImplementedError()

    def accept(self, visitor):
        """
        TODO: Implement
        """
        raise NotImplementedError()
