from bs4 import BeautifulSoup as bs
import requests
from urllib.request import urlopen as ureq
import re
from selenium import webdriver

def findinglinks(soup , links ,directories):
    #adding data to file
    fsub = open("subdirectories.txt" , "w")
    #finding and storing all the a tags
    socialmedia=""
    directoriess = soup.findAll("a")
    for directory in directoriess:
        d = directory["href"]
        #finding links in a tags
        if(links.find(d) == -1 & directories.find(d) == -1):
            #vilidating links
            if "http" in d:
                #seperating social media sites
                sites = ('facebook','twitter','youtube','insta','github')
                if any(s in d for s in sites):
                    socialmedia = socialmedia + d + "\n"
                else:
                    links = links + d + "\n"
            elif d[:1] == '/':
                    directories = directories + d +"\n"
                    fsub.write(d +"\n")
    return directories , links
    fsub.close()

def screenshot(url,name):
    #capturing screenshot
    BASE = 'https://render-tron.appspot.com/screenshot/'
    path = name + '.jpg'
    response = requests.get(BASE + url, stream=True)
    # save file, see https://stackoverflow.com/a/13137873/7665691
    if response.status_code == 200:
        with open(path, 'wb') as file:
            for chunk in response:
                file.write(chunk)

def indirect(value, soup):
    return {
        1: lambda soup: store(soup),
        2: lambda soup: marketplace(soup),
        3: lambda soup: enterprise(soup),
        4: lambda soup: "none",
        5: lambda soup: usecases(soup),
        6: lambda soup: success_stories(soup),
        7: lambda soup: "none",
        8: lambda soup: "none",
        9: lambda soup: proxy(soup),
        10: lambda soup: "none",
        11: lambda soup: "none",
        12: lambda soup: about(soup),
        13: lambda soup: contact(soup),
        14: lambda soup: "none",
        15: lambda soup: "none",
        16: lambda soup: "none",
        17: lambda soup: pricing(soup),
        18: lambda soup: "none",
        19: lambda soup: "none",
        20: lambda soup: "none",
        21: lambda soup: "none",
        22: lambda soup: "none",
        23: lambda soup: "none",
    }.get(value)(soup)

#1
def store(soup):
    # name the output file to write to local disk
    out_filename = "store.csv"
    # header of csv file to be written
    headers = "product name,product link,author,no of people \n"
    # opens file, and writes headers
    f=open(out_filename, "w")
    f.write(headers)
    #finding all div tags with particukar class
    containers = soup.findAll("div", {"class": "ActorCard__CardWrap-sc-1t63tgh-2 jOvyap"})
    for container in containers:
        #product name
        product_name= container.h6.string
        #product link
        product_link= container.p.string
        #author
        authorWrap= container.findAll("p",{"class":"Text__Small-j8cx6p-8 gTVhJq"})[0].text
        #popularity
        people= container.findAll("p",{"class":"Text__Small-j8cx6p-8 loYqgu"})[0].text

        # prints the dataset to console
        print("product name: " + product_name )
        print("product link: " + product_link )      
        print("author: " + authorWrap )
        print("no of people: " + people + "\n")
        
        # writes the dataset to file
        f.write(product_name + ", " + product_link + ", " + authorWrap +", " +people+ "\n")
    f.close()

#2
def marketplace(soup):
    #marketplace
    print("marketplace /n")
    print(soup.findAll("h2",{"class":"Text__H2-j8cx6p-1 cFscrW"})[0].text)
    containers = soup.findAll("h6",{"class":"Text__H6-j8cx6p-5 iSBVOD"})
    for container in containers:
        print(container.string)

#3
def enterprise(soup):
    print(soup.findAll("h2",{"class":"Text__H2-j8cx6p-1 cFscrW"})[2].text)
    containers = soup.findAll("h6",{"class":"Text__H6-j8cx6p-5 iSBVOD"})
    for i in range (22,29):
        print(containers[i].string)

#5
def usecases(soup):
    print("use-cases \n")
    containers = soup.findAll("h2",{"class":"Text__H5-j8cx6p-4 cuHLsx"})
    for container in containers:
        print(container.string)

#6
def success_stories(soup):
    print("Sucess Stories \n")
    containers = soup.findAll("h2",{"class":"Text__H5-j8cx6p-4 cuHLsx"})
    for container in containers:
        print(container.string)

#9
def proxy(soup):
    print(soup.findAll("h2",{"class":"Text__H2-j8cx6p-1 cFscrW"})[1].text)
    containers = soup.findAll("h6",{"class":"Text__H6-j8cx6p-5 iSBVOD"})
    for i in range (22,28):
        print(containers[i].string)

#12
def about(soup):
    containers = soup.findAll("div",{"class","about__Person-nefy6g-1 fjmMOv"})
    clean = re.compile('<.*?>')
    for container in containers:
        person = re.sub(clean,'  ', str(container))
        print(person)

#13
def contact(soup):
    print("contact")
    address = soup.findAll("div",{"class":"src__Box-sc-1sbtrzs-0 CleanedBox-sc-2gyvdq-0 ggqJYb buMEib"})[1]
    other= soup.findAll("div",{"class":"src__Box-sc-1sbtrzs-0 CleanedBox-sc-2gyvdq-0 bxBHKu buMEib"})[1]
    clean = re.compile('<.*?>')
    address = re.sub(clean,' ', str(address))
    other = re.sub(clean,' ', str(other))
    print(address)
    print(other)

#17
def pricing(soup):
    #opening a csv file
    f=open("pricing.csv", "w")
    #giving headers
    f.write("user,,,currency,price,,duration \n")
    print("price")
    team = soup.findAll("div",{"class" : "card-header"})
    price = soup.findAll("div",{"class" : "ComponentTransition__Fade-sc-1oq4ivb-1 khuwUR"})
    clean = re.compile('<.*?>')
    for i in range (0,5):
        user=team[i].text
        print(user)
        price_time = re.sub(clean,', ', str(price[i]))
        print(price_time)
        f.write(user + "," + price_time + "\n")
    f.close()
    
                        
#main program

url="https://apify.com/"

#downloading html in file webele
webele = ureq(url)
#transfering html to soup
soup = bs(webele.read(), "html.parser")
#closing file
webele.close()

#finding and storing all the a tags
directoriess = soup.findAll("a")

#setting no value
#links
links = ""
#directories
directories = ""
#social media accounts
socialmedia = ""
#string
s="http"

# name the output file to write to local disk
out_filename = "links.txt"
# opens file
f = open("directories.txt" , "w")
# opens file
a = open(out_filename, "w")

for directory in directoriess:
    #storing value in attribute href
    d = directory["href"]
    #finding links in a tags
    if(links.find(d) == -1 & directories.find(d) == -1):
        #vilidating links
        if "http" in d:
            #seperating social media sites
            if "facebook" in d:
                socialmedia = socialmedia + d + "\n"
            elif "twitter" in d:
                socialmedia = socialmedia + d + "\n"
            elif "youtube" in d:
                socialmedia = socialmedia + d + "\n"
            elif "insta" in d:
                socialmedia = socialmedia + d + "\n"
            elif "github" in d:
                socialmedia = socialmedia + d + "\n"
            else:
                links = links + d + "\n"
                a.write(d + "\n")
        elif d[:1] == '/':
            directories = directories + d + "\n"
            f.write(d + "\n")
f.close()
a.close()
            
for x in range(0, 5):
    print(" press 1: about site \n press 2: links \n press 3: social media")
    print(" press 4: directories \n press 5: screenshot\n press any other no. to exit")
    num = input("enter number ")
    num = int(num)
    if num == 1:
        # get attributes:
        print(soup.title.name)
        # get values:
        print(soup.title.string)
        print(soup.h2.string)
        # beginning navigation:
        print(soup.title.parent.name)
    elif num == 2:
        print(links)
    elif num == 3:
        print(socialmedia)
    elif num == 4:
        print(directories)
    elif num == 5:
        screenshot(url,"apify")
    else:
       break

#segmenting
directories = directories.split("\n")

x=1
x = int(x)
#setting no value
sub_directories=""

for x in range(1,25):
    print("press 0 to exit")
    i=0
    i=int(i)
    for x in range(1,25):
        print(i ,directories[i][1:len(directories[i])])
        i=i+1
    x = input("enter number ")
    if x == '0':
        break
    #downloading html in file webele
    webele = ureq(url + directories[int(x)])
    #transfering html to soup
    soup = bs(webele.read(), "html.parser")
    #closing file
    webele.close()
    for y in range(0, 4):
        print("press 1: about site \n press 2: links \n press 3: screenshot")
        print(" press 4: directories \n press 5: findings\n press any other no to exit")
        num = input("enter number ")
        num = int(num)
        if num == 1:
            # get attributes:
            print(soup.title.name)
            # get values:
            print(soup.title.string)
            #checking if h1 tag is present
            if(soup.findAll("h1")!=[]):
                print(soup.h1.string)
            #checking if h2 tag is present
            if(soup.findAll("h2")!=[]):
                print(soup.h2.string)
            # beginning navigation:
            print(soup.title.parent.name)
        elif num == 2:
            sub_directories , links = findinglinks(soup , links ,sub_directories)
            print(links)
        elif num == 3:            
            screenshot(url,directories[int(x)][1:])
        elif num == 4:
            sub_directories , links = findinglinks(soup , links ,sub_directories)
            print(sub_directories)
        elif num == 5:
            indirect(int(x), soup)
        else:
           break        



