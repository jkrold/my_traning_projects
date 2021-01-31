import rdflib
from rdflib.namespace import DC, DCTERMS, DOAP, FOAF, SKOS, OWL, RDF, RDFS, VOID, XMLNS, XSD

g = rdflib.Graph()
g.load('http://dbpedia.org/resource/Semantic_Web')

for s, p, o in g:
    print(s, p, o)

semweb = rdflib.URIRef('http://dbpedia.org/resource/Semantic_Web')
type = g.value(semweb, rdflib.RDFS.label)

g.add((
    rdflib.URIRef("http://example.com/person/nick"),
    FOAF.givenName,
    rdflib.Literal("Nick", datatype=XSD.string)
))