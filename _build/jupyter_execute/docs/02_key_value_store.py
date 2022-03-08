#!/usr/bin/env python
# coding: utf-8

# # Workbook 02 - Quick Start with Key Value Store
# 
# Macrometa GDN is a geodistributed real-time coordination-free materialized views engine that supports multiple data models. You can use GDN as a geo-replicated real-time key-value datastore or database.
# 
# If you are new to Macrometa GDN, start by reading the essentials of Macrometa GDN.
# 
# Each document stored in a collection (or table) contains a primary key _key. The rest of the document is considered a value. The collection behaves like a simple key-value (KV) store if it has no secondary indexes.
# 
# The key-value store has no query languages. The permissible operations are key look-ups (single & batch) and key-value pair insertions, updates and deletions. If you don't specify a sharding attribute, we use _key to shard the data. The simplicity of this model makes a key-value store fast, easy to use, scalable, portable, and flexible.
# 
# You can enable time_to_live (TTL) during collection creation and add an expireAt value to specify the expiration time for each document in the KV collection.
# 
# For the following examples, assume these credentials:

# ## Pre-requisite
# 
# Lets Assume 
# - you have already made a tenant account, and have a username and password
# - you have installed the pyc8 drivers as explained in section 01
# - you have generated an API Key as explained in section 01
# 

# ## Step 02-A - Connect to GDN
# 
# The first step in using GDN is to establish a connection to a local region. When this code executes, it initializes the server connection to the region URL you sepcified. You can create an API key from the GUI or REST API.
# 

# In[ ]:


import json

from c8 import C8Client
client = C8Client(protocol='https', host='gdn.paas.macrometa.io', port=443,
                        email='[email]', password='[xxxx]',
                        geofabric='_system')

# OR Using token

#client = C8Client(protocol='https', host='gdn.paas.macrometa.io', port=443, token="XXXX")


# ## Step 02-B - Create a Collection

# In[ ]:


collection_name = "students"

# Create a new collection if it does not exist
if client.has_collection(collection_name):
    print("Collection exists")
else:
    client.create_collection_kv(name=collection_name)
    print("Collection Created!")


# ## Step 02-C - Insert Key Value Pairs
# 
# Insert key-value pairs into the collection.

# In[ ]:


data = [
  {
    "_key": "John",
    "value": "Science",
    "expireAt": 0
  },
  {
    "_key": "Alice",
    "value": "Maths",
    "expireAt": 0
  },
  {
    "_key": "Alex",
    "value": "Physics",
    "expireAt": 0
  },
  {
    "_key": "Monika",
    "value": "Chemistry",
    "expireAt": 0
  }
]

client.insert_key_value_pair(collection_name, data)
print("KV Pairs Inserted")


# ## Step 02-D - Get a Value
# 
# Get value for a given key.

# In[ ]:


#print("Value for the provided key: ",client.get_value_for_key(collection_name, "Monika"))

value = client.get_value_for_key(collection_name, "John")

print(json.dumps(value, indent=4))


# ## Step 02-E - Get Key-Value Count
# 
# Get key-value count from a given collection

# In[ ]:


print("Number of kv pairs in your collection: ",client.get_kv_count(collection_name))


# ## Step 02-F - Update Value
# 
# Update value for a given key

# In[ ]:


# Update value for a key
data = {
    "_key": "John",
    "value": "Biology",
    "expireAt": 0
}
client.insert_key_value_pair(collection_name, data)
print("Updated the specified KV pair")


# ## Step 02-G - Delete a Key-Value
# 
# Delete key-value pairs from a collection

# In[ ]:


# Delete entry for a key
print("Deleted Entry for the specified Key: ",client.delete_entry_for_key(collection_name, "John"))


# ## Step 02-H - Delete a Key-Value
# 
# Delete entry for multiple key-value pairs from a collection

# In[ ]:


# Delete entry for multiple keys

# -- Simple line of code --

#print("Deleted Entries for the list of keys: ",client.delete_entry_for_keys(collection_name, ["Monika", "Alex", "Alice"]))

# -- Elegant lines of code for easier reading --

value2 = client.delete_entry_for_keys(collection_name, ["Monika", "Alex", "Alice"])
print("Deleted Entries for the following list of keys:")
print(json.dumps(value2, indent=4))


# ## Step 02-I - Delete a Collection
# 
# Delete the key-vlaue collection

# In[ ]:


print("Collection Deleted: ",client.delete_collection_kv(collection_name))


# ## Workbook Completed!
# 
# Congratulations you should have successfuly create a collection, inserted values, updated a value, deleted an entry, delted all entries and finally deleted the collection. 
# 
# Dont forget you can log into your GDN account and check the console to see what is happening from the dashboard at the same time!

# In[ ]:




