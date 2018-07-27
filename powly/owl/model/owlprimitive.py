from abc import abstractmethod, ABC

from powly.owl.model.owlobject import OWLObject


class OWLPrimitive(OWLObject, ABC):
    """
    A common interface for: OWLClass, OWLObjectProperty, OWLDataProperty,
    OWLAnnotationProperty, OWLDatatype, OWLAnonymousIndividual, OWLLiteral, IRI
    i.e. the basic "leaf" objects that are used in axioms, class expressions and
    annotations.
    """

    @abstractmethod
    def __init__(self, *args):
        pass
