from abc import abstractmethod

from powly.owl.model.hasannotationvalue import HasAnnotationValue
from powly.owl.model.hasannotations import HasAnnotations
from powly.owl.model.hasproperty import HasProperty
from powly.owl.model.owlobject import OWLObject

# TODO: Check OWLAnnotationImplNotAnnotated
class OWLAnnotation(OWLObject, HasAnnotations, HasProperty, HasAnnotationValue):  #, OWLAnnotationNotAnnotated):
    def components_without_annotations(self):
        raise NotImplementedError()

    def components(self):
        raise NotImplementedError()

    def components_annotations_first(self):
        raise NotImplementedError()

    @abstractmethod
    def get_property(self):
        """
        Gets the property that this annotation acts along.

        :return: The annotation property
        """
        pass

    @abstractmethod
    def get_value(self):
        """
        Gets the annotation value. The type of value will depend upon the type
        of the annotation e.g. whether the annotation is an OWLLiteral, an
        IRI or an OWLAnonymousIndividual.

        :return: The annotation value
        """
        pass