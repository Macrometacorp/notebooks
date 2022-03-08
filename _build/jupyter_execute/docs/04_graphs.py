#!/usr/bin/env python
# coding: utf-8

# # Workbook 04 - Quick Start with Graphs
# 
# ## Overview
# 
# Today’s applications are required to be highly responsive and always online. They need to be deployed in datacenters closer to their users and can access data instantly across the globe.
# 
# Macrometa global data network (GDN) is a fully managed realtime materialzed view engine that provides access to data instantly to Apps & APIs in a simple & single interface.
# 
# This article is an introduction to working with documents in GDN with pyC8 and jsC8 drivers.
# 
# In the drivers, a document is a dictionary/object that is JSON serializable with the following properties:
# 
# Contains the _key field, which identifies the document uniquely within a specific collection.
# Contains the _id field (also called the handle), which identifies the document uniquely across all collections within a fabric. This ID is a combination of the collection name and the document key using the format {collection}/{key} (see example below).
# Contains the _rev field. GDN supports MVCC (Multiple Version Concurrency Control) and is capable of storing each document in multiple revisions. Latest revision of a document is indicated by this field. The field is populated by GDN and is not required as input unless you want to validate a document against its current revision.
# Here is an example of a valid document:

# In[1]:


{
    '_id': 'students/bruce',
    '_key': 'bruce',
    '_rev': '_Wm3dzEi--_',
    'first_name': 'Bruce',
    'last_name': 'Wayne',
    'address': {
        'street' : '1007 Mountain Dr.',
        'city': 'Gotham',
        'state': 'NJ'
    },
    'is_rich': True,
    'friends': ['robin', 'gordon']
}


# Edge documents (edges) are similar to standard documents but with two additional required fields _from and _to. Values of these fields must be the handles of "from" and "to" vertex documents linked by the edge document in question. Here is an example of a valid edge document:

# In[2]:


{
    '_id': 'friends/001',
    '_key': '001',
    '_rev': '_Wm3dyle--_',
    '_from': 'students/john',
    '_to': 'students/jane',
    'closeness': 9.5
}


# A Graph consists of vertices and edges. Edges are stored as documents in edge collections. A vertex can be a document of a document collection or of an edge collection (so edges can be used as vertices). Which collections are used within a named graph is defined via edge definitions. A named graph can contain more than one edge definition, at least one is needed. Graphs allow you to structure your models in line with your domain and group them logically in collections and giving you the power to query them in the same graph queries.
# 
# In SQL you commonly have the construct of a relation table to store n:m relations between two data tables. An edge collection is somewhat similar to these relation tables. Vertex collections resemble the data tables with the objects to connect.
# 
# While simple graph queries with fixed number of hops via the relation table may be doable in SQL with several nested joins, graph databases can handle an arbitrary number of these hops over edge collections - this is called traversal. Also edges in one edge collection may point to several vertex collections. Its common to have attributes attached to edges, i.e. a label naming this interconnection.
# 
# Edges have a direction, with their relations _from and _to pointing from one document to another document stored in vertex collections. In queries you can define in which directions the edge relations may be followed i.e.,
# 
# - OUTBOUND: _from → _to
# - INBOUND: _from ← _to
# - ANY: _from ↔ _to.

# ## Pre-requisite
# 
# Lets Assume 
# - you have already made a tenant account, and have a username and password
# - you have installed the pyc8 drivers as explained in section 01
# - you have generated an API Key as explained in section 01
# - you have imported the json driver, no? run the next cell!
# 

# In[3]:


# Run this Cell so that you can output any C8QL results in JSON Format!
import json


# ## Step 04-A - Connect to GDN

# In[4]:


from c8 import C8Client
client = C8Client(protocol='https', host='gdn.paas.macrometa.io', port=443,
                        email='[email]', password='[XXXX]',
                        geofabric='_system')

# OR Using token

#client = C8Client(protocol='https', host='gdn.paas.macrometa.io', port=443, token="XXXX")


# ## Step 04-B - Get GeoFabric Details
# 
# To get details of fabric,

# In[ ]:


# you might not need this, but if you wanted to select a 
# specific GeoFabric you can find out whats available by executing this code!

print("Get geo fabric details...")

# -- use this line of code for an unformated response --
#print(client.get_fabric_details())

# -- use these lines of code for a formated response (easier to read) -- 
import json

fabrics = client.get_fabric_details()

print(json.dumps(fabrics, indent=4))


# ## Step 04-C - Create Collection
# 
# We can now create collection in the fabric. To do this, first you connect to fabric and then create a collection called employees.
# 
# The below example shows the steps.

# In[ ]:


collection_name = 'employees'

# Create a new collection if it does not exist
if client.has_collection(collection_name):
    print("Collection exists")
else:
    client.create_collection_kv(name=collection_name)
    print("Collection Created!")


# ## Step 04-D - Create an Edge Collection
# 
# An edge collection contains edge documents and shares its namespace with all other types of collections. You can manage edge documents via standard collection API wrappers, but using edge collection API wrappers provides additional safeguards:
# 
# - All modifications are executed in transactions.
# - Edge documents are checked against the edge definitions on insert.

# In[ ]:


# Simple Approach
#client = C8Client(protocol='https', host='gdn.paas.macrometa.io', port=443,
#                        email='[email protected]', password="xxxxxx",
#                        geofabric='_system')

edge_name='school'

if client.has_collection(edge_name):
  print("Graph exists")
else:
  client.create_collection(edge_name, edge=True)
  print("Created Edge Collection")   


# ## Step 04-E - Insert Documents
# 
# Let's insert documents to the students collection as shown below.

# In[ ]:


docs = [
  {'_key':'Jenny', 'firstname': 'Jenney', 'lastname':'Jones', 'email':'[email protected]'},
  {'_key':'Bob', 'firstname': 'Bob', 'lastname':'Billy', 'email':'[email protected]'},
  {'_key':'Alan', 'firstname': 'Alan', 'lastname':'Evans', 'email':'[email protected]'}
]

client.insert_document(collection_name='students', document=docs)

print(json.dumps(docs, indent=4))


# ## Step 04-F - Create Graph
# 
# A graph consists of vertices and edges. Vertices are stored as documents in vertex collections and edges stored as documents in edge collections. The collections used in a graph and their relations are specified with edge definitions.

# In[ ]:


if client.has_graph('school'):
    school = client.has_graph('school')
    print("Graph Exists")
else:
    school = client.create_graph('school')
    print("Graph Created")


# ## Section Completed!
# 
# TBC...

# In[ ]:




