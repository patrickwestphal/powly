from powly.owl.model.owllogicalaxiom import OWLLogicalAxiom


class OWLPropertyAxiom(OWLLogicalAxiom):
    def __init__(self, annotations=None):
        """
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(annotations)
