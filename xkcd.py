#download all xkcd comics
from bs4 import BeautifulSoup as bs
import urllib
import requests
import re

url = 'https://www.xkcd.com/'

pages = range(1749)

def download(soup):
    div = soup.find('div', id='comic')
    title = soup.find('title')
    name = str(title).replace("<title>","")
    not_allowed = ['<title>','</title>','\\','/',':','*','?','<','>','|']
    for ch in not_allowed:
        if ch in name:
            name = name.replace(ch,"")      
    data = str(div.contents[1])
    urls = re.findall('//(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data)
    url_final = "https:"+urls[0]
    urllib.request.urlretrieve(url_final,"C:\\Python34\\xkcd\\"+str(name)+".png")
        
def parse(img):
        try:
            html = urllib.request.urlopen(img)
            soup = bs(html,"html.parser")
            download(soup)
            print("------- "+str(img)+" :Done -------")            
        except urllib.error.HTTPError as e:
            print(e)
        except:
            pass

def main():
    for i in pages:
        img = url + str(i)
        parse(img)
    print("XKCD...Complete")
main()
