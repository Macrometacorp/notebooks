#!/usr/bin/env python
# coding: utf-8

# # Workbook 03 - Quick Start with Documents Store
# 
# Documents in GDN are JSON objects. These objects can be nested (to any depth) and may contain lists. Each document has a unique primary key which identifies it within its collection. Furthermore, each document is uniquely identified by its document handle across all collections. Different revisions of the same document (identified by its handle) can be distinguished by their document revision. Any transaction only ever sees a single revision of a document.
# 
# For example:

# In[1]:


{
  "_id" : "myusers/3456789",
  "_key" : "3456789",
  "_rev" : "14253647",
  "firstName" : "John",
  "lastName" : "Doe",
  "address" : {
    "street" : "Road To Nowhere 1",
    "city" : "Gotham"
  },
  "hobbies" : [
    {name: "swimming", howFavorite: 10},
    {name: "biking", howFavorite: 6},
    {name: "programming", howFavorite: 4}
  ]
}


# All documents contain special attributes:
# 
# - the document handle is stored as a string in _id,
# - the document's primary key in _key and
# - the document revision in _rev.
# 
# The value of the _key attribute can be specified by the user when creating a document. _id and _key values are immutable once the document has been created. The _rev value is maintained by GDN automatically.

# ## Pre-requisite
# 
# Lets Assume 
# - you have already made a tenant account, and have a username and password
# - you have installed the pyc8 drivers as explained in section 01
# - you have generated an API Key as explained in section 01
# - you have imported the json driver, no? run the next cell!
# 

# In[ ]:


# Run this Cell so that you can output any C8QL results in JSON Format!
import json


# ## Step 03-A - Connect to GDN

# In[ ]:


from c8 import C8Client
client = C8Client(protocol='https', host='gdn.paas.macrometa.io', port=443,
                        email='[email]', password='[xxxx]',
                        geofabric='_system')

# OR Using token

#client = C8Client(protocol='https', host='gdn.paas.macrometa.io', port=443, token="XXXX")


# ## Step 03-B - Get GeoFabric Details
# 
# To get details of fabric,

# In[ ]:


# you might not need this, but if you wanted to select a 
# specific GeoFabric you can find out whats available by executing this code!

print("Get geo fabric details...")

# -- use this line of code for an unformated response --
#print(client.get_fabric_details())

# -- use these lines of code for a formated response (easier to read) -- 
fabrics = client.get_fabric_details()

print(json.dumps(fabrics, indent=4))


# ## Step 03-C - Create Collection
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


# ## Step 03-D - Create Index
# 
# Let's add a hash_index called emails to our collection employees. Please refer to reference guide for details on other available index types.

# In[ ]:


# Simple Approach

#print("Add Hash Index", client.add_hash_index('employees', fields=['firstname', 'lastname'], unique=True)
#)                      

print("Add Hash Index")

hash_index = client.add_hash_index('employees', fields=['firstname', 'lastname'], unique=True)

print(json.dumps(hash_index, indent=4))


# ## Step 03-E - Insert Documents
# 
# Let's insert documents to the employees collection as shown below.

# In[ ]:


#client.insert_document(collection_name='employees', document={'_key':'Alan', 'firstname': 'Alan', 'lastname':'Evans', 'email':'[email protected]'})

docs = [
  {'_key':'James', 'firstname': 'James', 'lastname':'Kirk', 'email':'[email protected]'},
  {'_key':'Han', 'firstname': 'Han', 'lastname':'Solo', 'email':'[email protected]'},
  {'_key':'Bruce', 'firstname': 'Bruce', 'lastname':'Wayne', 'email':'[email protected]'}
]

client.insert_document(collection_name='employees', document=docs)

print(json.dumps(docs, indent=4))


# ## Step 03-F - Query documents using C8QL
# 
# 8QL is C8's query language. You can execute C8QL query on our newly created collection employees to get its contents.
# 
# The query "FOR employee IN employees RETURN employee" is equivalent to SQL's SELECT query.

# In[ ]:


cursor = client.execute_query('FOR employee IN employees RETURN employee')

#cursor = client.execute_query("for d in tutorial_coll return d")
docs = [document for document in cursor]


print(json.dumps(docs, indent=4))


# ## Step 03-G - Get realtime updates
# 
# Example for real-time updates from a collection in fabric:
# 
# Note: for this to work you need to enable Stream from the Macrometa Dashboard. Do this by opening up the dashboard, sellect collections, find the collection named "employees" and select "enable Stream"
# 
# Now run the cell below, return to the MAcrometa Dashboard ans modeify and save fields in the collection. you should see the real time updates below as soon as you hit save!. 
# 
# the websocket will time out after 60sec if no updates are seen, so you might need to re run the cell code if youy see a timed out messege below. :)

# In[ ]:


def callback_fn(event):
    print(event)

client.on_change("employees", callback=callback_fn)     


# ## Section Completed!
# 
# TBC...

# In[ ]:




