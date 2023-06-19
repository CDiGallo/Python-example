import json
import pandas as pd

from IPython.display import  HTML #JSON,
#from js import Object, fetch
#from io import StringIO
print("Hello World")

from SPARQLWrapper import SPARQLWrapper, JSON, TURTLE #JSON; TURTLE sind was zurückgegeben werden kann. mehr dazu: https://sparqlwrapper.readthedocs.io/_/downloads/en/latest/pdf/ Seite 8

sparql = SPARQLWrapper(
    "https://ld.admin.ch/query"
) #hier ist der api-endpoint
sparql.setReturnFormat(CSV) # hier kann auch TURTLE oder JSON stehen

# get more or less random data
# WEnn wir triples zurückwollen, dann müssen wir describe oder Construct nehmen. WEil sonst will er es automatisch konvertieren. 
sparql.setQuery("""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT DISTINCT ?s ?p ?l
    WHERE {
  ?s ?p ?l.
  (?l ?score) <tag:stardog:api:property:textMatch> 'Swiss Federal Archives'.
    }

limit 10
 """
)

try:
   ret = sparql.queryAndConvert() #das ist vom workexample von sparqlwarpper. es wird in ret gespeichert und konvertiert und dann keine ahnung, was es macht. 

  for r in ret["results"]["bindings"]:
     print(r)
except Exception as e:
    print(e)
