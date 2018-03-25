
import numpy as np 
import scipy as sp 
# % matplotlib inline
# import matplotlib as plt 
import pandas as pd
import json 

# TO LOAD: 
# - List of blacklisted websites: CSV of ['link without http://', 4 digit number 0111]
# - List of good websites: CSV of ['link without http://'] 
# 
# INPUT = url string
# 
# OUTPUT = [{'AuthorYN': 0-2, 'SiteYN': 0-2, 'Explanation': 01111}]
# - Author/Site YN number: 0 non-fiable, 1 fiable, 2 unknown
# - Explanation: 1er: publie des conspirations / 2eme: encourage de la méfiance envers les médias 
#   / 3eme: encourage de la méfiance envers la science / 4eme: ne distingue pas opinion des faits

# In[]:
blacklist = pd.read_csv('blacklist.csv',header=None)
goodlist = pd.read_csv('goodlist.csv',header=None)

# In[]:

def rulebased(url):
    author = 2  #won't be changed lol
    site = 2 
    expl = '0000'
    domain = url.split('/')[2]
    checkbad = 0
    for i in range(len(blacklist[0])):
#         print(domain)
        if (blacklist[0][i]==domain):
            site=0 #not reliable
            checkbad=1
            expl = str(blacklist[1][i]).zfill(4)
    if(checkbad==0):
        for j in range(len(goodlist[0])):
            if(goodlist[0][j]==domain):
                site=1 #reliable 
    return json.dumps({'AuthorYN': author, 'SiteYN': site, 'Explanation': expl},)
#     otherwise site=1 reliable

