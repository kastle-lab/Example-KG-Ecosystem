import csv

# open the text file
with open("us-fips.txt", "r") as file:

    # create an empty list to store the dictionaries
    county_list = []

    # iterate through each line in the file
    for line in file:

        # split the line into a list of values
        values = line.strip().split(",")

        # assign the values to variables representing each field
        state_code = values[0]
        state_fips = values[1]
        county_fips = values[2]
        county_name = values[3]
        county_id = values[4]

        # create a dictionary with the field names as keys and the values as values
        county_dict = {
            "state_code": state_code,
            "state_fips": state_fips,
            "county_fips": county_fips,
            "county_name": county_name,
            "county_id": county_id
        }
        

        # add the dictionary to the list
        county_list.append(county_dict)

# print the list of dictionaries
print(county_list[10])




state_codes = {}
with open('state_codes.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        state_codes[row[1]] = row[0]
for item in county_list:
    item['state_name'] = state_codes.get(item['state_code'])

# Print the updated dictionary list including now state names.
print(county_list[10])

from rdflib import Namespace, Graph, Literal, RDF, URIRef

# Create an RDF graph
g = Graph()

# Define the namespaces
kastle = Namespace("http://kastle.com/")
schema = Namespace("http://schema.org/")

# Loop through the list of dictionaries and add the data to the graph
for item in county_list:
    county_name = item.get('county_name')
    state_name = item.get('state_name')
    if county_name is not None:
        county_name = county_name.replace(' ', '_')
    if 'state_name' in county_list:
       state_name = county_list['state_name']
    else:
       state_name = ''

    subject = kastle[county_name + '_' + state_name]
    state_code = item['state_code']
    state_fips = item['state_fips']
    county_fips = item['county_fips']
    county_id = item['county_id']
    
    state = kastle[state_code]

    # Add triples to the graph
    g.add((subject, RDF.type, schema.Place))
    g.add((subject, kastle.hasCountyName, Literal(item['county_name'])))
    g.add((subject, kastle.hasCountyCode, Literal(county_fips)))
    g.add((subject, kastle.hasCountyFIPS, Literal(item['county_fips'])))
    g.add((subject, kastle.hasCountyID, Literal(item['county_id'])))
    g.add((subject, kastle.hasStateCode, state))
    g.add((subject, kastle.hasStateName, Literal(item['state_name'])))
    g.add((state, RDF.type, schema.Place))
    g.add((state, kastle.hasStateCode, Literal(state_code)))
    g.add((state, kastle.hasStateFIPS, Literal(state_fips)))

# Print the graph
g.serialize(destination='my_graph.ttl', format='turtle')

                
