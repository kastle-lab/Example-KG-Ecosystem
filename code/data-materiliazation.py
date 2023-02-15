import csv
"""
# Read in the text file and create a dictionary with state codes as keys and a list of counties as values
county_dict = {}
with open('us-fips.txt', 'r') as f:
    for line in f:
        state_code, state_fips, county_fips, county_name, county_ID = line.strip().split(',')
        if state_code not in county_dict:
            county_dict[state_code] = []
        county_dict[state_code].append(county_name)
        print(county_dict.items())
    """
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



"""
# define the key to search for
search_key = 'state_code'

# create an empty list to store the values for the search key
values_list = []

# loop through the list of dictionaries and append the values for the search key to the values list
for item in county_list:
    if search_key in item:
        values_list.append(item[search_key])

# print the values list
print(values_list)
"""
"""
with open('state_codes.csv') as csvfile:
    reader = csv.reader(csvfile)
    # iterate over each row in the CSV file
    for row in reader:
        # assuming the state code is in the first column of the CSV file
        state_code_ = row[1]
        state_name=row[0]
        print(state_code_)
        print(state_name)
        for v in values_list:
            if v==state_code_:
                item=state_name
                for item in county_list:
                    print(item)
"""

state_codes = {}
with open('state_codes.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        state_codes[row[1]] = row[0]
for item in county_list:
    item['state_name'] = state_codes.get(item['state_code'])

# Print the updated dictionary list
print(county_list[10])
from rdflib import Namespace, Graph, Literal, RDF, URIRef

# Create an RDF graph
g = Graph()

# Define the namespaces
ex = Namespace("http://example.com/")
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

    subject = ex[county_name + '_' + state_name]
    state_code = item['state_code']
    state_fips = item['state_fips']
    county_fips = item['county_fips']
    county_id = item['county_id']
    
    state = ex[state_code]

    # Add triples to the graph
    g.add((subject, RDF.type, schema.Place))
    g.add((subject, ex.hasCountyName, Literal(item['county_name'])))
    g.add((subject, ex.hasCountyCode, Literal(county_fips)))
    g.add((subject, ex.hasCountyFIPS, Literal(item['county_fips'])))
    g.add((subject, ex.hasCountyID, Literal(item['county_id'])))
    g.add((subject, ex.hasStateCode, state))
    g.add((subject, ex.hasStateName, Literal(item['state_name'])))
    g.add((state, RDF.type, schema.Place))
    g.add((state, ex.hasStateCode, Literal(state_code)))
    g.add((state, ex.hasStateFIPS, Literal(state_fips)))

# Print the graph
g.serialize(destination='my_graph.ttl', format='turtle')

                
"""
# Read in the csv file and create a dictionary with state codes as keys and state names as values
state_dict = {}
with open('state_codes.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        state_dict[row[0]] = row[1]

# Output a dictionary with state names as keys and a list of counties in that state as values
output_dict = {}
for state_code, county_list in county_dict.items():
    state_name = state_dict[state_code]
    if state_name not in output_dict:
        output_dict[state_name] = []
    output_dict[state_name].extend(county_list)

print(output_dict)
"""
