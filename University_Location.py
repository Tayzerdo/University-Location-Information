# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 11:55:26 2020

@author: tayze
"""

import urllib.parse, urllib.error, urllib.request
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = ' '
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input ('Enter the University location: ')
    if len(address)<1: break
    parms=dict()
    parms['address']=address
    if api_key is not False: parms['key']=api_key
    url=serviceurl+urllib.parse.urlencode(parms)
    
    print('Retrieving',url)
    uh=urllib.request.urlopen(url, context=ctx)
    data=uh.read().decode()
    print('Retrieved',len(data),'characters')
    
    try:
        js=json.loads(data)
    except:
        js=None
    
    if not js or 'status' not in js or js['status']!='OK':
        print('====== Failure to rerived =====')
        print(data)
        continue
    print(" ")
    print(address)
    print('Place id',js['results'][0]['place_id'])
    print('The address is:',js['results'][0]['formatted_address'])
    print('The Lat is',js['results'][0]['geometry']['location']['lat'])
    print('The Long is',js['results'][0]['geometry']['location']['lng'])
