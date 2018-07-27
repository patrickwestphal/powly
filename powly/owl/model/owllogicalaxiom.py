from owl.model.owlaxiom import OWLAxiom


class OWLLogicalAxiom(OWLAxiom):
    def __init__(self, annotations=None):
        super().__init__(annotations)

    @staticmethod
    def is_logical_axiom():
        return True
