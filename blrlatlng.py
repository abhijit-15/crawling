import csv
import os
from requests.utils import quote
import requests, json, re

key = "0e41de65-d2c5-4ebd-9cfb-a552dae27f3e"
header = {'referer': 'http://large-analytics.flipkart.com/'}
rev_geoCodeAPI = "http://10.85.50.71/reverse-geocode?key="+str(key)+"&point="

def get_pincode(lat,lng):
    point = quote(str(lat) + ',' + str(lng),safe='')
    url1 = rev_geoCodeAPI + point 
    url1 = re.sub(r'#', r'', url1)
    resp = requests.get(url1, headers=header, timeout=None)
    pincode = json.loads(resp.text)
    return pincode['results'][0]['pincodes'][0]

f = open('C:/Users/phatak.a/Desktop/Blr_Lat_Lng.csv','w',newline='' )
data = []
csvw = csv.writer(f,delimiter=',')
for i in range(1,66):
    for j in range(1,72):
        try: #Based on the bounding box
            lat = 12.7996+0.005*(i-1) 
            lng = 77.4259+0.005*(j-1)
            data += [(str(lat),str(lng),str(get_pincode(lat,lng)))]
            print((str(lat),str(lng),str(get_pincode(lat,lng))))
        except:
            print("could not find " + str(lat) + " " + str(lng))
            continue
        
csvw.writerows(data)
f.close()
