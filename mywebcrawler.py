from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
import re

class parentdir:
    def __init__(self,url,directory = None):
        self.directory=directory
        self.url = url
        #the parameters to be taken come under this function
    directories=""
    links=""
    soup=""
    socialmedia=""
    sno=0

    def callurl(self):        
        #downloading html
        r= requests.get(self.url)
        #transfering html to soup
        self.soup = bs(r.text, "html.parser")
        #print(self.soup)

    def findinglinks(self):
        #adding data to file
        fsub = open("directories.txt" , "w")
        #finding and storing all the a tag
        directoriess = self.soup.findAll("a")
        d=""
        for directory in directoriess:
            #directory = bs(directory,"html.parser")
            d = directory.get('href')
            d= str(d)
            #finding links in a tags
            if(self.links.find(d) == -1 & self.directories.find(d) == -1):
                #vilidating links
                if "http" in d:
                    #seperating social media sites
                    sites = ('facebook','twitter','youtube','insta','github')
                    if any(s in d for s in sites):
                        self.socialmedia = self.socialmedia + d + "\n"
                    else:
                        self.links = self.links + d + "\n"
                 
                elif re.search("^(\/)\w",d ):
                    if self.sno == 0:
                        self.directories = self.directories + d +"\n"
                        fsub.write(d +"\n")
                    else:
                        self.directories = self.directories + self.directory[int(self.sno) -1] + d +"\n"
        fsub.close()
    
    def screenshot(self):
        #assigning file name
        for i in range (0,4):
            name = "screen"+str(i)+".png"
        #taking screenshot
        driver = webdriver.Firefox()
        driver.get(self.url)
        driver.get_screenshot_as_file(name)
        driver.close()

    def saveimage(self):
        d=self.soup.findAll("img")
        img =""
        count =0
        for e in d:
            k= e.get('src')    
            if re.search("^(\/\/)\w", k): 
                print(k)
                img = img + k +"\n"
                count = count +1
            elif re.search("http",k):
                print(k)
                img = img + k +"\n"
                count = count +1
        if count == 0:
            print("none found")
        img = img.split("\n")

        for i in range(count):
            print()
            no=input("enter number below " + str(count) +" to exit enter any other no ")
            no= int(no)
            if no > count:
                break
            if re.search("^(\/\/)\w", img[no] ):
                r= requests.get( 'https:' + str(img[no]))
            else:
                r= requests.get(str(img[no]))
            name = "image"+str(i)+".png"
            with open (name,'wb') as f:
                f.write(r.content)

    def output(self):
        self.findinglinks()
        for x in range(0, 6):
            print(" press 1: about site \n press 2: links \n press 3: screenshot")
            print(" press 4: directories \n press 5: social media \n press 6: saving image \n press any other key to exit ")
            num = input("enter number ")
            num = int(num)
            if num == 1:
                # get attributes:
                print(self.soup.title.name)
                # get values:
                print(self.soup.title.string)
                #checking if h1 tag is present
                if(self.soup.findAll("h1")!=[]):
                    print(self.soup.h1.string)
                #checking if h2 tag is present
                if(self.soup.findAll("h2")!=[]):
                    print(self.soup.h2.string)
                # beginning navigation:
                print(self.soup.title.parent.name)
            elif num == 2:
                if self.links!="":
                    print(self.links)
                else:
                    print("none found")
            elif num == 3:            
                self.screenshot()
            elif num == 4:
                if self.directories!="":
                    print(self.directories)
                else:
                    print("none found")
            elif num ==5:
                if self.socialmedia!="":
                    print(self.socialmedia)
                else:
                    print("none found")
            elif num ==6:
                self.saveimage()
            else:
                break

    def finddir(self):
        for x in range (0, len(self.directory)):              
            i=0
            i=int(i)
            for d in self.directory:
                #printing names of directories
                print(i+1 ,self.directory[i][1 : len(self.directory[i])])
                i=i+1
            print("press 0 to exit")
            self.sno = input("enter number ")
            if self.sno == '0':
                break
            else:
                r= requests.get(self.url + self.directory[int(self.sno) - 1])
                #transfering html to soup
                self.soup = bs(r.text, "html.parser")
                #print(self.soup)
                self.output()
    
    def giveback(self):
        #converting directories to list
        self.directories = self.directories.split("\n")
        #returning directories
        return self.directories


#main code
url= input("enter url ")
#calling the url
par = parentdir(url)
par.callurl()
par.output()
#taking values of directories
give = par.giveback()

if len(give) == 0: 
    depth = 0
    depth = input("depth = ")

    for i in range(int(depth)):
        direc = parentdir(url,give)
        direc.finddir()
        give = direc.giveback()
        
