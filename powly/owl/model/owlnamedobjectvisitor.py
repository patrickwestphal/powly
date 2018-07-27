from abc import abstractmethod, ABC

from powly.owl.model.owlentityvisitor import OWLEntityVisitor


class OWLNamedObjectVisitor(OWLEntityVisitor, ABC):
    @abstractmethod
    def visit(self, entity):
        """
        :param entity: Object of one of the following classes: OWLOntology; or
        of one of these classes: OWLClass, OWLDatatype,
        OWLNamedIndividual, OWLAnnotationProperty, OWLDataProperty,
        OWLObjectProperty
        """
        pass
