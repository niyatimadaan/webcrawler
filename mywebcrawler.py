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
# getting specific values:
print(soup.p)

#finding and storing all the a tags
directoriess = soup.findAll("a")
#setting no value
directories = ""

for directory in directoriess:
    d = directory["href"]
    directories = directories + d

print(directories)

    
            
    



