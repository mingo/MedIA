#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 11:25:32 2018

@author: peterchen
"""

import requests, json, re

def strip(htmltxt):
    return re.sub('(<[^>]*>)', '', htmltxt)

def getRC(url):
    try:
        if url.find('radio-canada') != -1:
            numbers = list(map(int, re.findall(r'\d+', url)))
            ID = numbers.pop()
            
            while ID not in range(1000000, 1100000):
                ID = numbers.pop()
            
            url = 'https://services.radio-canada.ca/hackathon/neuro/v1/news-stories/' \
                + str(ID) + '?client_key=bf9ac6d8-9ad8-4124-a63c-7b7bdf22a2ee'
            
            r = requests.get(url)
            parsed = json.loads(r.content)
            
            return strip(parsed['body']['html'])
        
    except:
        return ''