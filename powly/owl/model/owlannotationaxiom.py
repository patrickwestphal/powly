from powly.owl.model.owlannotationobject import OWLAnnotationObject
from powly.owl.model.owlaxiom import OWLAxiom


class OWLAnnotationAxiom(OWLAxiom, OWLAnnotationObject):
    """A super interface for annotation axioms"""

    def is_annotation_axiom(self):
        return True
