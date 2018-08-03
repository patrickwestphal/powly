from powly.owl.model.owlnaryaxiom import OWLNaryAxiom
from powly.owl.model.owlobject import OWLObject
from powly.owl.model.owlpropertyaxiom import OWLPropertyAxiom


class OWLNaryPropertyAxiom(OWLPropertyAxiom, OWLNaryAxiom):
    def __init__(self, properties, annotations=None):
        """
        :param properties: A list or stream of OWLPropertyExpression objects
        :param annotations:
        """
        super().__init__(annotations)
        self.properties = properties
        self.properties.sort()

    def __hash__(self):
        hsh = self.hash_index()
        hsh = OWLObject.hash_iteration(hsh, hash(self.get_operands_as_list()))
        return OWLObject.hash_iteration(hsh, hash(self.annotations_as_list()))

    def components(self):
        """TODO: Implement"""
        raise NotImplementedError()

    def components_without_annotations(self):
        """TODO: Implement"""
        raise NotImplementedError()

    def components_annotations_first(self):
        """TODO: Implement"""
        raise NotImplementedError()

    def properties(self):
        """
        :return: all of the properties that appear in this axiom
        """
        return (p for p in set(self.properties))

    def operands(self):
        return self.properties()

    def get_operands_as_list(self):
        return self.properties

    def get_properties_minus(self, property):
        """
        :param property: property the property to skip
        :return: the set of properties minus property
        """
        return set(self.properties).difference(set(property))
