from enum import Enum


class Status(Enum):
    LEGACY = 1
    IN_USE = 2


class BuiltIn(Enum):
    BUILT_IN = 1
    NOT_BUILT_IN = 2


class Namespaces(Enum):
    OWL2 = ('owl2', 'http://www.w3.org/2006/12/owl2#', Status.LEGACY)
    OWL11XML = \
        ('owl11xml', 'http://www.w3.org/2006/12/owl11-xml#', Status.LEGACY)
    OWL11 = ('owl11', 'http://www.w3.org/2006/12/owl11#', Status.LEGACY)
    OWL = ('owl', 'http://www.w3.org/2002/07/owl#', Status.IN_USE)
    RDFS = ('rdfs', 'http://www.w3.org/2000/01/rdf-schema#', Status.IN_USE)
    RDF = ('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#', Status.IN_USE)
    XSD = ('xsd', 'http://www.w3.org/2001/XMLSchema#', Status.IN_USE)
    XML = ('xml', 'http://www.w3.org/XML/1998/namespace')
    SWRL = ('swrl', 'http://www.w3.org/2003/11/swrl#')
    SWRLB = ('swrlb', 'http://www.w3.org/2003/11/swrlb#')
    SKOS = ('skos', 'http://www.w3.org/2004/02/skos/core#')

    GRDDL = ('grddl', 'http://www.w3.org/2003/g/data-view#')
    MA = ('ma', 'http://www.w3.org/ns/ma-ont#')
    PROV = ('prov', 'http://www.w3.org/ns/prov#')
    RDFA = ('rdfa', 'http://www.w3.org/ns/rdfa#')
    RIF = ('rif', 'http://www.w3.org/2007/rif#')
    R2RML = ('rr', 'http://www.w3.org/ns/r2rml#')
    SD = ('sd', 'http://www.w3.org/ns/sparql-service-description#')
    SKOSXL = ('skosxl', 'http://www.w3.org/2008/05/skos-xl#')
    POWDER = ('wdr', 'http://www.w3.org/2007/05/powder#')
    VOID = ('void', 'http://rdfs.org/ns/void#')
    POWDERS = ('wdrs', 'http://www.w3.org/2007/05/powder-s#')
    XHV = ('xhv', 'http://www.w3.org/1999/xhtml/vocab#')
    ORG = ('org', 'http://www.w3.org/ns/org#')
    GLDP = ('gldp', 'http://www.w3.org/ns/people#')
    CNT = ('cnt', 'http://www.w3.org/2008/content#')
    DCAT = ('dcat', 'http://www.w3.org/ns/dcat#')
    EARL = ('earl', 'http://www.w3.org/ns/earl#')
    HT = ('ht', 'http://www.w3.org/2006/http#')
    PTR = ('ptr', 'http://www.w3.org/2009/pointers#')

    CC = ('cc', 'http://creativecommons.org/ns#')
    CTAG = ('ctag', 'http://commontag.org/ns#')
    DCTERMS = ('dcterms', 'http://purl.org/dc/terms/')
    DC = ('dc', 'http://purl.org/dc/elements/1.1/')
    FOAF = ('foaf', 'http://xmlns.com/foaf/0.1/')
    GR = ('gr', 'http://purl.org/goodrelations/v1#')
    ICAL = ('ical', 'http://www.w3.org/2002/12/cal/icaltzd#')
    OG = ('og', 'http://ogp.me/ns#')
    REV = ('rev', 'http://purl.org/stuff/rev#')
    SIOC = ('sioc', 'http://rdfs.org/sioc/ns#')
    VCARD = ('vcard', 'http://www.w3.org/2006/vcard/ns#')
    SCHEMA = ('schema', 'http://schema.org/')
    GEO = ('geo', 'http://www.w3.org/2003/01/geo/wgs84_pos#')
    SC = ('sc', 'http://purl.org/science/owl/sciencecommons/')
    FB = ('fb', 'http://rdf.freebase.com/ns/', Status.LEGACY)
    GEONAMES = ('geonames', 'http://www.geonames.org/ontology#', Status.LEGACY)
    DBPEDIA = ('dbpedia', 'http://dbpedia.org/resource/')
    DBP = ('dbp', 'http://dbpedia.org/property/')
    DBO = ('dbo', 'http://dbpedia.org/ontology/')
    YAGO = ('yago', 'http://dbpedia.org/class/yago/')

    def __init__(
            self, prefix, ns, status=Status.IN_USE,
            built_in=BuiltIn.NOT_BUILT_IN):
        """
        :param prefix: A
        :param ns:
        :param status:
        :param built_in:
        """
        self.prefix = prefix
        self.ns = ns
        self.status = status
        self.built_in = built_in
        if ns[0] in ['/', '#']:
            self.hashless = ns[:-1]
        else:
            self.hashless = ns

    def get_prefix_name(self):
        return self.prefix

    def __str__(self):
        return self.ns
