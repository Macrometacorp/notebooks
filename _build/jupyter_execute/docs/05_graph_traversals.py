#!/usr/bin/env python
# coding: utf-8

# # Workbook 05 - Graph Traverals
# 
# ## Overview
# 
# A graph consists of vertices and edges. Vertices are stored as documents in vertex collections and edges stored as documents in edge collections. The collections used in a graph and their relations are specified with edge definitions.

# In[1]:


from c8 import C8Client
import pprint

# Variables - Queries
global_url = "gdn.paas.macrometa.io"
email = "[email]" # <-- Email goes here
password = "[xxxxx]" # <-- password goes here
geo_fabric = "_system"
collection_people = "CDRpeople"
collection_calls = "CDRcalls"
collection_cellsites = "CDRcellsites"
collection_graph = "CDRgraphdocs"
read_people = "FOR person IN CDRpeople RETURN person"
read_calls = "FOR call IN CDRcalls RETURN call"
person = "Lou Feaveer"
graph_traversal1 = "FOR c IN CDRpeople FILTER c.full_name == \"{}\" FOR v IN 1..1 INBOUND c CDRcalls RETURN v".format(person)
graph_traversal2 = "FOR c IN CDRpeople FILTER c.full_name == \"{}\" FOR v IN 1..1 OUTBOUND c CDRcalls RETURN v".format(person)

pp = pprint.PrettyPrinter(indent=4)

# Initialize the C8 Data Fabric client.
# Step1: Open connection to GDN. You will be routed to closest region.
#print("1. CONNECT: federation: {},  user: {}".format(global_url, email))
#client = C8Client(protocol='https', host='gdn.paas.macrometa.io', port=443)

# For the "mytenant" tenant, connect to "test" fabric as tenant admin.
# This returns an API wrapper for the "test" fabric on tenant 'mytenant'
# Note that the 'mytenant' tenant should already exist.
#tenant = client.tenant(email, password)
#fabric = tenant.useFabric('_system')


client = C8Client(protocol='https', host='gdn.paas.macrometa.io', port=443,
                        email='alan@macrometa.com', password='AKScorpio74GDN!',
                        geofabric='_system')


# Step2: Create collections if not exists
print("2a. CREATE_PEOPLE_VERTEX_COLLECTION: region: {},  collection: {}".format(global_url, collection_people))
if client.has_collection(collection_people):
    peopleCol = client.collection(collection_people)
else:
    peopleCol = client.create_collection(collection_people)

print("2b. CREATE_CALLS_EDGE_COLLECTION: region: {},  collection: {}".format(global_url, collection_calls))
if client.has_collection(collection_calls):
    callsCol = client.collection(collection_calls)
else:
    callsCol = client.create_collection(collection_calls, edge=True)

# Step3: Insert data into collections.
print("3a. INSERT_PEOPLE_DATA: region: {}, collection: {}".format(global_url, collection_people))

# insert documents into the collection
docs = [
  {
    "full_name": "Kiel Dummer",
    "first_name": "Kiel",
    "last_name": "Dummer",
    "city": "Burbank",
    "state": "CA",
    "address": "40317 5th Crossing",
    "calling_nbr": "757-697-9065",
    "_key": "757-697-9065"
  },
  {
    "full_name": "Pernell Winspare",
    "first_name": "Pernell",
    "last_name": "Winspare",
    "city": "San Diego",
    "state": "CA",
    "address": "596 Packers Pass",
    "calling_nbr": "718-208-8096",
    "_key": "718-208-8096"
  },
  {
    "full_name": "Ava Kermath",
    "first_name": "Ava",
    "last_name": "Kermath",
    "city": "Berkeley",
    "state": "CA",
    "address": "2 Doe Crossing Junction",
    "calling_nbr": "765-623-5328",
    "_key": "765-623-5328"
  },
  {
    "full_name": "Tremain McGrah",
    "first_name": "Tremain",
    "last_name": "McGrah",
    "city": "Torrance",
    "state": "CA",
    "address": "079 Russell Street",
    "calling_nbr": "859-783-3227",
    "_key": "859-783-3227"
  },
  {
    "full_name": "Vidovik Boddam",
    "first_name": "Vidovik",
    "last_name": "Boddam",
    "city": "Los Angeles",
    "state": "CA",
    "address": "3 Brentwood Crossing",
    "calling_nbr": "703-265-1313",
    "_key": "703-265-1313"
  },
  {
    "full_name": "Oralie Goward",
    "first_name": "Oralie",
    "last_name": "Goward",
    "city": "Los Angeles",
    "state": "CA",
    "address": "922 Columbus Park",
    "calling_nbr": "617-815-8610",
    "_key": "617-815-8610"
  },
  {
    "full_name": "Lou Feaveer",
    "first_name": "Lou",
    "last_name": "Feaveer",
    "city": "San Jose",
    "state": "CA",
    "address": "55223 Hooker Crossing",
    "calling_nbr": "716-463-8993",
    "_key": "716-463-8993"
  },
  {
    "full_name": "Peria King",
    "first_name": "Peria",
    "last_name": "King",
    "city": "Stockton",
    "state": "CA",
    "address": "8 Troy Plaza",
    "calling_nbr": "713-707-8699",
    "_key": "713-707-8699"
  }
]
peopleCol.insert_many(docs)

print("3a. INSERT_CALL_RECORDS_DATA: region: {}, collection: {}".format(global_url, collection_calls))
docs = [
        {
    "calling_nbr": "757-697-9065",
    "called_nbr": "716-463-8993",
    "_from": "CDRpeople/757-697-9065",
    "_to": "CDRpeople/716-463-8993",
    "call_date": "1/4/2020",
    "call_time": "13:33",
    "call_duration": 30,
    "cell_site": 4044703906
  },
  {
    "calling_nbr": "716-463-8993",
    "called_nbr": "713-707-8699",
    "_from": "CDRpeople/716-463-8993",
    "_to": "CDRpeople/713-707-8699",
    "call_date": "1/28/2020",
    "call_time": "3:02",
    "call_duration": 18,
    "cell_site": 2289973823
  },
  {
    "calling_nbr": "765-623-5328",
    "called_nbr": "713-707-8699",
    "_from": "CDRpeople/765-623-5328",
    "_to": "CDRpeople/713-707-8699",
    "call_date": "1/28/2020",
    "call_time": "3:02",
    "call_duration": 18,
    "cell_site": 2289973823
  }
    ]
callsCol.insert_many(docs)

#Step4: Create a graph
print("4. CREATE_GRAPH...CDRgraph")
graph = client.create_graph(collection_graph)
register = graph.create_edge_definition(
        edge_collection=collection_calls,
        from_vertex_collections=[collection_people],
        to_vertex_collections=[collection_people]
    )


# In[2]:


#Step5: Read Data
print("5a. GRAPH_TRAVERSAL: Find outbound calls TO: {}".format(person))
cursor = client.execute_query(graph_traversal1)
docs = [document for document in cursor]
pp.pprint(docs)


# In[3]:


print("5b. GRAPH_TRAVERSAL: Find inbound calls FROM: {}".format(person))
cursor = client.execute_query(graph_traversal2)
docs = [document for document in cursor]
pp.pprint(docs)


# In[4]:


# Step6: Delete Data
print("6. DELETE_DATA...")
#callsCol.truncate()
#peopleCol.truncate()
#client.delete_graph(graph, drop_collections=False)

client.delete_graph(collection_graph, drop_collections=False)


# ## Section Completed!
# 
# TBC...

# In[ ]:




