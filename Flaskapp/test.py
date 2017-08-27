from flask import Flask, render_template,request,redirect
from bs4 import BeautifulSoup
import requests
import sys
import os

#given_url = 'https://www.yellowpages.ca/search/si/1/Food%20Delivery/toronto'
given_url = 'https://bulbapedia.bulbagarden.net/wiki/eevee'
#secnd_url = 'http://www.smogon.com/dex/dp/pokemon/pikachu/'
#url = 'https://www.newegg.ca/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

#This is how you connect the script with the client site
open_url = requests.get(given_url)
#open_sec_url = requests.get(secnd_url)   
soup = BeautifulSoup(open_url.content, "lxml")
#soup_two = BeautifulSoup(open_sec_url.content,"lxml")
#image_txt = 'alt = {0}'.format(text)
#try:
links = soup.find("table", {"class" : "roundy"} , {"style" : "max-width:420px;"})
name = links.find("big").text
catogory = links.find("span", {"style" : "color:#000;"}).text
picture = links.find("img")
type = links.find("span" , {"style" : "color:#FFF;"}, "b").text


#print(soup_two.prettify())

#for li in soup_two:
 #   lin = soup_two.find("div")
   
  #  print(lin);


ablity = links.find_all("table",{"class" : "roundy"},{"style" : "max-width:420px;"})
table_lists = []
table_ablity_list = []
table_field_list = []
table_otherinfo_list = []

for abl in ablity:
    yolo = abl.find_all("span",{"style" : "color:#000;"},"Cacophony")
    if yolo:
        #print(yolo)
        table_lists.append(yolo)
        
table_lists2 = list(set(table_lists[1])) 
    
for abl in table_lists[3]:
    table_field_list.append(abl)
    
    
otherinfor = links.find_all("table",{"class" : "roundy"},{"width" : "100%"})

for oi in otherinfor:
    #print("\n")
    #print ("*************************************************")
    yoloone = oi.find("td").text
    #print(str(yoloone).encode("utf-8"))
    #print ("*************************************************")
    #print("\n")
    table_otherinfo_list.append(yoloone)
    


print ("name: ",name)
print ("catagorey : ", catogory)
print ("picture : ", picture)
print ("type :", type)
for abl in table_lists2:
    print("ablity :",abl.text)

print ("catch rate :", table_otherinfo_list[5])
print ("egg type : ",table_otherinfo_list[6])


for li in table_otherinfo_list:
    print("*************************")
    print(li.encode("utf-8"))
    print("*************************")
    
   # print(str(oi).encode('utf8'))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#print(table_field_list[1])

#ablity = links.find_all("tr")
#print(soup.prettify().encode('utf-8'))
#print(links.encode('utf-8'))

#for li in ablity:
 #   print("--------------")
  #  print(li.find("table",{"class" : "roundy"}).encode('utf-8'))
   # print("---------------")
#abl = ablity[2].find("span")

#print("hello")
#for abl in ablity[2]:
    #print ("hello", file=sys.stderr)
#    print (abl.text, file=sys.stderr)
    
#for catch in ablity[4]:
 #   print (str(abl), file=sys.stderr)

#for link in ablity:
 #   for li in link:
        #print (str(li), file=sys.stderr)
  #      print ("************************************", file=sys.stderr)
        #print (str(ablity[2]), file=sys.stderr)
   #     print ("***********************************", file=sys.stderr)
    #print("-----------------------------------------", file=sys.stderr)
    #print(link.text)
    #print(link.contents[1].find_all("table","a","href"), file=sys.stderr)
#except:
 #   pass