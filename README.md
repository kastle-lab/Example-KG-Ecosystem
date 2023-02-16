## Data :
The data is in a form of a dictionary containing the state codes and FIPS codes along with the state names, the county IDS and FIPS codes and names. 

## Output :
 A turtle file containing the information for each county/state along with said codes.
 
 ## Schema :
 The schema diagram can be found [here.](https://github.com/kastle-lab/Example-KG-Ecosystem/blob/example-updates/schema/KL-Example.png)

## Example Output :
ns1:Abbeville_County_ a <<http://schema.org/Place>> ; 

    ns1:hasCountyCode "001" ;
    ns1:hasCountyFIPS "001" ;
    ns1:hasCountyID "H1" ;
    ns1:hasCountyName "Abbeville County" ;
    ns1:hasStateCode ns1:SC ;
    ns1:hasStateName "South Carolina" .
Which shows the county name, county FIPS along with countyID and state code and name.

## Contributors : 

* Cogan Shimizu
* Antrea Christou


