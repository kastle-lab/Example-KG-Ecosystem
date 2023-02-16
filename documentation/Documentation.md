## Overview
Connecting FIPS codes for counties and states with corresponding county names / IDs and state names.

## Competency Questions and SPARQL Queries :
5. What are the county names and state names in the graph?

SELECT ?countyName ?stateName
WHERE {
  ?county kastle:hasCountyName ?countyName .
  ?county kastle:hasStateName ?stateName .
}
4. How many counties are in each state?

SELECT ?stateName (COUNT(?county) AS ?countyCount)
WHERE {
  ?county kastle:hasStateName ?stateName .
}
GROUP BY ?stateName
3. What are the county IDs for counties in Georgia?


SELECT ?countyID
WHERE {
  ?county kastle:hasStateName "Georgia" .
  ?county kastle:hasCountyID ?countyID .
}
 

## Use Cases
Providing knowledge about a place in the United States based on their FIPS Code, county name and ID and state name.

## Formatilization


## Submodules


## Views 


## Entanglements


## Examples

## Contributors

* Cogan Shimizu
* Antrea Christou


