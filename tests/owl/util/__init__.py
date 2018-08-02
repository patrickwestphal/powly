from unittest import TestCase

from powly.owl.model.owlclass import OWLClass
from powly.owl.model.owldisjointclassesaxiom import OWLDisjointClassesAxiom
from powly.owl.model.owlobjectintersectionof import OWLObjectIntersectionOf
from powly.owl.model.owlobjectproperty import OWLObjectProperty
from powly.owl.model.owlobjectsomevaluesfrom import OWLObjectSomeValuesFrom


class TestFlattenFunctions(TestCase):
    def test_flat_components(self):
        prefix = 'http://example.com#'
        cls1 = OWLClass(prefix + 'Class1')
        cls2 = OWLClass(prefix + 'Class2')
        cls3 = OWLClass(prefix + 'Class3')
        cls4 = OWLClass(prefix + 'Class4')
        cls5 = OWLClass(prefix + 'Class5')
        cls6 = OWLClass(prefix + 'Class6')
        cls7 = OWLClass(prefix + 'Class7')
        cls8 = OWLClass(prefix + 'Class8')
        op1 = OWLObjectProperty(prefix + 'objProp1')
        op2 = OWLObjectProperty(prefix + 'objProp2')
        op3 = OWLObjectProperty(prefix + 'objProp3')
        ce1 = OWLObjectSomeValuesFrom(op1, cls4)
        ce2 = OWLObjectSomeValuesFrom(
            op2,
            OWLObjectIntersectionOf([cls5, cls6]))
        ce3 = OWLObjectSomeValuesFrom(op3, ce2)

        # Class1
        axiom = OWLDisjointClassesAxiom([cls1])
        self.assertEquals(axiom.components(), [classmethod])
