#Grab image of FSN from fk

import requests
import urllib
from bs4 import BeautifulSoup as bs

fsn_list = ['TVSE8FMZ8ASXHGYW','TVSE8FMZ9AQMEGC6','TVSEZUBU4VP2VC98']

url = 'https://www.flipkart.com/item/'

def get_image(soup):
    div = soup.findAll('img',{"class":"sfescn"})
    item = div[0]
    replaced = str(item).replace('"',"").split('=')
    for obj in replaced:
        if '.jpeg' in obj:
            img_url = obj[:-2]
    return img_url

def parse(img):
    try:
        html = urllib.request.urlopen(url+img)
        soup = bs(html,"html.parser")
        url_final = get_image(soup)
        #print(url_final)
        urllib.request.urlretrieve(url_final,"C:\\Python34\\fk_fsn\\"+str(img)+".jpeg")
        k = "------- "+str(img)+" :Done -------"            
    except urllib.error.HTTPError as e:
        k = e
    except:
        k = print(str(img)+" unsuccessful :( ")
        pass
    return k


for i in fsn_list:
    print(parse(i))
