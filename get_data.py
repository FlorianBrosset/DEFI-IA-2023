#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 00:24:08 2022

@author: bun-kim
"""

import urllib.parse

domain = "51.91.251.0"
port = 3000
host = f"http://{domain}:{port}"
path = lambda x: urllib.parse.urljoin(host, x)

import requests

user_id = '545115b6-c8cf-4dbd-9e1c-a8270ea9bd66'
name = 'max-4th-avatar'
r = requests.post(path(f'avatars/{user_id}/{name}'))


r = requests.post(path(f"avatars/{user_id}/{name}"))
r = requests.get(path(f"avatars/{user_id}"))
for avatar in r.json():
    print(avatar['id'], avatar['name'])

# =============================================================================
# 
# =============================================================================

dates = [4,3,2,1,0]
langues = ["dutch","danish","spanish","french","italian","bulgarian","maltese","austrian","lithuanian" ,"greek"]
villes= ["amsterdam", "copenhagen", "madrid", "paris", "rome", "sofia", "valletta", "vienna","vilnius"]
mobiles = [0]

# =============================================================================
# 
# =============================================================================

DATA = []
for date in dates:
    for langue in langues:
        for ville in villes:
            for mobile in mobiles :
                params = {
                    "avatar_name": "max-5th-avatar",
                    "language": langue,
                    "city": ville,
                    "date": date,
                    "mobile": mobile,
                }
                r = requests.get(path(f"pricing/{user_id}"), params=params)
                DATA.append(r)
                r.json()
                
test = []
for date in dates:
    for langue in langues:
        for ville in villes:
            for mobile in mobiles :
                test.append([date,langue,ville,mobile])
                
# =============================================================================
#         
# =============================================================================
        
all_DATA =[]
for k in range(len(DATA)):
    all_DATA.append(DATA[k].json())        
                
len(all_DATA)               

true_data = DATA[:]
                
                

                
                
# =============================================================================
# 
# =============================================================================

import pandas as pd

pricing_requests = []
compteur= 0 
requests = true_data
for r in requests:
    compteur +=1
    print(compteur)
    try:
        pricing_requests.append(
            pd.DataFrame(r.json()['prices']).assign(**r.json()['request']))
    except  KeyError : 
        None
pricing_requests = pd.concat(pricing_requests)
pricing_requests.head()



infile = '/home/bun-kim/Documents/price_to_merge.csv'

pricing_requests.to_csv(infile)




