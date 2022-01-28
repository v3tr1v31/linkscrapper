import requests
import os
from bs4 import BeautifulSoup

global urls #allows urls to be used as one function everywhere
urls = []
i = 0
def scrapper(x,y): #finds urls
        for link in x.find_all('a', href=True):
            with open(y, 'a+') as file:
                file.write(link['href'] + "\n")
def repscrapper(): #used for follows
    with open("temp.txt") as f:
        for line in f:
            if not line.startswith('http'):
                pass
            else:
                try:
                    get = requests.get(line)
                    soup = BeautifulSoup(get.text, 'html.parser')
                    scrapper(soup,'out.txt')
                except:
                    continue
        
url = input('Enter a URL to scrape for links and subdomains. (ex: https://google.com)\n') #asks for url
fol = input('How many follows should be performed?\n') #asks for amount of follows
fol = int(fol)
get = requests.get(url)
soup = BeautifulSoup(get.text, 'html.parser')
scrapper(soup,'temp.txt') #initial grab of all urls

while i<=fol: #follows initial urls
    repscrapper()
    i=i+1

os.remove('temp.txt') #removes temp files