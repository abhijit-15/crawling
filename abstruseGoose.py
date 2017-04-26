#download all xkcd comics
from bs4 import BeautifulSoup as bs
import urllib
import requests
import re

url = 'http://www.abstrusegoose.com/'

pages = range(576)
#pages = range(2)

def download(soup):
    div = soup.findAll('img') 
    for item in div:
        if 'http://abstrusegoose.com/strips/' in str(item):
            url_base = str(item).replace('"',"").split('=')
    for item in url_base:
        if '.png' in item:
            url_final = str(item).replace(" title","").strip(' ')
    title = soup.find('title')
    name = str(title).replace("<title>","")
    not_allowed = ['<title>','</title>','\\','/',':','*','?','<','>','|']
    for ch in not_allowed:
        if ch in name:
            name = name.replace(ch,"")      
    urllib.request.urlretrieve(url_final,"C:\\Python34\\abstrusegoose\\"+str(name)+".png")
    
def parse(img):
        try:
            html = urllib.request.urlopen(img)
            soup = bs(html,"html.parser")
            download(soup)
            print("------- "+str(img)+" :Done -------")            
        except urllib.error.HTTPError as e:
            print(e)
        except:
            print(str(img)+" unsuccessful :( ")
            pass

def main():
    for i in pages:
        img = url + str(i)
        parse(img)
    print("Completed")
main()
