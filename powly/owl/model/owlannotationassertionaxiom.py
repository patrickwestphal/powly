from powly.owl.model.owlannotation import OWLAnnotation
from powly.owl.model.owlobject import OWLObject
from powly.owl.model.hasannotationvalue import HasAnnotationValue
from powly.owl.model.hasproperty import HasProperty
from powly.owl.model.hassubject import HasSubject
from powly.owl.model.owlannotationaxiom import OWLAnnotationAxiom


class OWLAnnotationAssertionAxiom(
            OWLAnnotationAxiom, HasSubject, HasProperty, HasAnnotationValue):

    def __init__(self, subject, property, value, annotations=None):
        """
        :param subject: An OWLAnnotationSubject object
        :param property: An OWLAnnotationProperty object
        :param value: An OWLAnnotationValue object
        :param annotations: A collection of OWLAnnotation objects
        """
        super().__init__(annotations)
        assert subject is not None
        self.subject = subject
        assert property is not None
        self.property = property
        assert value is not None
        self.value = value

    def hash_index(self):
        return 47

    def components(self):
        raise NotImplementedError()

    def components_without_annotations(self):
        raise NotImplementedError()

    def __hash__(self):
        hsh = self.hash_index()
        hsh = OWLObject.hash_iteration(hsh, hash(self.get_subject()))
        hsh = OWLObject.hash_iteration(hsh, hash(self.get_property()))
        hsh = OWLObject.hash_iteration(hsh, hash(self.get_value()))
        return OWLObject.hash_iteration(hsh, hash(self.annotations_as_list()))

    def components_annotations_first(self):
        raise NotImplementedError()

    def get_value(self):
        """
        :return: An OWLAnnotationValue object
        """
        return self.value

    def get_property(self):
        return self.property

    def get_subject(self):
        return self.subject

    def get_annotation(self):
        """
        :return: An OWLAnnotation object
        """
        return OWLAnnotation(self.property, self.value)

    def is_deprecated_iri_assertion(self):
        """
        Determines if this annotation assertion deprecates the IRI that is
        the subject of the annotation.
        """
        return self.property.is_deprecated() and \
               self.get_annotation().is_deprecated_iri_annotation()

    def get_annotated_axiom(self, annotations):
        """
        :param annotations: A generator of OWLAnnotation objects
        """
        raise NotImplementedError()

    def get_axiom_without_annotations(self):
        raise NotImplementedError()

    def accept(self, visitor):
        raise NotImplementedError()

    def get_axiom_type(self):
        from powly.owl.model.axiomtype import AxiomType
        return AxiomType.ANNOTATION_ASSERTION

    def annotation_value(self):
        raise NotImplementedError()
