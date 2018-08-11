from powly.owl.model.hasannotationvalue import HasAnnotationValue
from powly.owl.model.owlannotationobject import OWLAnnotationObject
from powly.owl.model.owlprimitive import OWLPrimitive


class OWLAnnotationValue(OWLAnnotationObject, OWLPrimitive, HasAnnotationValue):
    def accept(self, visitor):
        raise NotImplementedError()

    def as_literal(self):
        raise NotImplementedError()

    def is_literal(self):
        return False

    def annotation_value(self):
        return self
