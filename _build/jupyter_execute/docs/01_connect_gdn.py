#!/usr/bin/env python
# coding: utf-8

# # Workbook 01 - Connecting to GDN

# ## Pre-requisite
# 
# Let's assume your 
# 
# - tenant name is [email protected] and
# - user password is xxxxx.
# 

# ## Step 01-A - Driver download
# 
# pyC8 requires Python 3.5+. Python 3.6 or higher is recommended
# 
# To install pyC8, simply run the following code in the cell below

# In[ ]:


# Run this code to install pyC8

get_ipython().system('pip install pyC8')


# ## Step 01-B - Connect to GDN
# 
# The first step in using GDN is to establish a connection to a local region. When this code executes, it initializes the server connection to the region URL you sepcified. You can create an API key from the GUI or REST API.

# In[ ]:


from c8 import C8Client
client = C8Client(protocol='https', host='gdn.paas.macrometa.io', port=443,
                        email='[email]', password='[xxxx]',
                        geofabric='_system')

# OR Using token
#client = C8Client(protocol='https', host='gdn.paas.macrometa.io', port=443, token="XXXX")


# ## Step 01-C - Create an API Key
# 
# Note: If you have already run the following cell to create your API Key, running it again will produce an error. you might like to remove the current API Key buy jumping to the section "## Remove an API Key" and then returning to this cell to create the API Key again.

# In[ ]:


print("Create API Key: ", client.create_api_key('id1'))


# ## Step 01-D - Get Accessible Resources

# In[13]:


# Fetch List of accessible databases and streams

print("Accessible Databases: ", client.list_accessible_databases('id1'))

print("Accessible Streams of a db: ", client.list_accessible_streams('id1', '_system'))


# ## Workbook Completed!

# Congratulations you should have now connected to GDN, and checked to see what resources are available!
