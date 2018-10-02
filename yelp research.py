
# coding: utf-8

# In[13]:


from yelpapi import YelpAPI
from pprint import pprint


# In[6]:


yelp_api = YelpAPI("6JFAZOLb4tCd1IbWWsL6fGph_KpZQW4z5QRmrIXR0H9X23d1jDxnORB0uYrAgGSHVhtCeqjj1W-VHRGEr0zqjPKwtbcglOyiOZQ3yCgQhI7N6tYDLcOal4DqI1snW3Yx")


# In[66]:


search_results = yelp_api.search_query(term= "Filipino", location=["Renton, Wa","seattle, wa"])


# In[23]:


response = yelp_api.reviews_query(id='OqrtfhUcN_El1ClubBAVPQ')


# In[46]:


pprint(search_results.get('businesses')[0]['alias'])


# In[83]:


storelist = []
locationlist = ["Renton, Wa", "Seattle, WA", "Tacoma, WA", "Everett, WA", "Federal Way, WA"]
for location in locationlist:
    search_results = yelp_api.search_query(term= "Filipino", location=location)
    for i in range(len(search_results.get('businesses'))):
        storelist.append(search_results.get('businesses')[i]['name'] +  " " + search_results.get('businesses')[i]['location']['city'])


# In[84]:


storelist = list(set(storelist))


# In[85]:


storelist

