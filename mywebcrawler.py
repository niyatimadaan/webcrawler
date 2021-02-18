from bs4 import BeautifulSoup as bs
import requests
from urllib.request import urlopen as ureq

url="https://apify.com/"

#downloading html in file webele
webele = ureq(url)
#transfering html to soup
soup = bs(webele.read(), "html.parser")
#closing file
webele.close()

# title of the page
print(soup.title)
# get attributes:
print(soup.title.name)
# get values:
print(soup.title.string)
# beginning navigation:
print(soup.title.parent.name)

#finding and storing all the a tags
directoriess = soup.findAll("a")

#setting no value
directories = ""
#social media accounts
socialmedia = ""

for directory in directoriess:
    d = directory["href"]
    if(directories.find(d) == -1):
        if "http" in d:
            directories = directories + d + "\n"
            if "facebook" in d:
                socialmedia = socialmedia + d + "\n"
            if "twitter" in d:
                socialmedia = socialmedia + d + "\n"
            if "youtube" in d:
                socialmedia = socialmedia + d + "\n"
            if "insta" in d:
                socialmedia = socialmedia + d + "\n"
            if "github" in d:
                socialmedia = socialmedia + d + "\n"
            
   
print(directories)
print(socialmedia)
directories = directories.split("\n")
