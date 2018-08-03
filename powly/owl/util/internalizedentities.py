from powly.owl.model.owlannotationproperty import OWLAnnotationProperty
from powly.owl.model.owlclass import OWLClass
from powly.owl.model.owldataproperty import OWLDataProperty
from powly.owl.model.owldatatype import OWLDatatype
from powly.owl.model.owlliteralboolean import OWLLiteralBoolean
from powly.owl.model.owlobjectproperty import OWLObjectProperty
from powly.owl.vocab.owl2datatype import OWL2Datatype
from powly.owl.vocab.owlrdfvocabulary import OWLRDFVocabulary

OWL_THING = OWLClass(OWLRDFVocabulary.OWL_THING.iri)
OWL_NOTHING = OWLClass(OWLRDFVocabulary.OWL_NOTHING.iri)
OWL_TOP_OBJECT_PROPERTY = OWLObjectProperty(
    OWLRDFVocabulary.OWL_TOP_OBJECT_PROPERTY.iri)
OWL_BOTTOM_OBJECT_PROPERTY = OWLObjectProperty(
    OWLRDFVocabulary.OWL_BOTTOM_OBJECT_PROPERTY.iri)
OWL_TOP_DATA_PROPERTY = OWLDataProperty(
    OWLRDFVocabulary.OWL_TOP_DATA_PROPERTY.iri)
OWL_BOTTOM_DATA_PROPERTY = OWLDataProperty(
    OWLRDFVocabulary.OWL_BOTTOM_DATA_PROPERTY.iri)
RDFSLITERAL = OWLDatatype(OWL2Datatype.RDFS_LITERAL.iri)
RDFS_LABEL = OWLAnnotationProperty(OWLRDFVocabulary.RDFS_LABEL.iri)
RDFS_COMMENT = OWLAnnotationProperty(OWLRDFVocabulary.RDFS_COMMENT.iri)
RDFS_SEE_ALSO = OWLAnnotationProperty(OWLRDFVocabulary.RDFS_SEE_ALSO.iri)
RDFS_IS_DEFINED_BY = \
    OWLAnnotationProperty(OWLRDFVocabulary.RDFS_IS_DEFINED_BY.iri)
OWL_BACKWARD_COMPATIBLE_WITH = \
    OWLAnnotationProperty(OWLRDFVocabulary.OWL_BACKWARD_COMPATIBLE_WITH.iri)
OWL_INCOMPATIBLE_WITH = \
    OWLAnnotationProperty(OWLRDFVocabulary.OWL_INCOMPATIBLE_WITH.iri)
OWL_VERSION_INFO = OWLAnnotationProperty(OWLRDFVocabulary.OWL_VERSION_INFO.iri)
OWL_DEPRECATED = OWLAnnotationProperty(OWLRDFVocabulary.OWL_DEPRECATED.iri)
PLAIN = OWLDatatype(OWL2Datatype.RDF_PLAIN_LITERAL.iri)
LANGSTRING = OWLDatatype(OWL2Datatype.RDF_LANG_STRING.iri)
XSDBOOLEAN = OWLDatatype(OWL2Datatype.XSD_BOOLEAN.iri)
XSDDOUBLE = OWLDatatype(OWL2Datatype.XSD_DOUBLE.iri)
XSDFLOAT = OWLDatatype(OWL2Datatype.XSD_FLOAT.iri)
XSDINTEGER = OWLDatatype(OWL2Datatype.XSD_INTEGER.iri)
XSDSTRING = OWLDatatype(OWL2Datatype.XSD_STRING.iri)
TRUELITERAL = OWLLiteralBoolean(True)
FALSELITERAL = OWLLiteralBoolean(False)
