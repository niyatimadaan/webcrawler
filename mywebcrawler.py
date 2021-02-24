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

def screenshot(url):
    #capturing screenshot
    driver = webdriver.Chrome()
    driver.get(url)
    driver.save_screenshot("C:\\Users\\ssd\\Desktop\\webcrawler")
    driver.close()

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
            
for x in range(0, 4):
    print(" press 1: about site \n press 2: links \n press 3: social media")
    print(" press 4: directories \n press 5: screenshot\n press any other key to exit")
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
        screenshot(url)
    else:
       break

#segmenting
directories = directories.split("\n")

x=1
x = int(x)
#setting no value
sub_directories=""

for x in range(1,26):
    print("press 0 to exit")
    i=0
    i=int(i)
    for x in range(1,26):
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
    for x in range(0, 4):
        print("press 1: about site \n press 2: links \n press 3: screenshot")
        print(" press 4: directories \n press any other key to exit")
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
            screenshot(url)
        elif num == 4:
            sub_directories , links = findinglinks(soup , links ,sub_directories)
            print(sub_directories)
        else:
           break        



