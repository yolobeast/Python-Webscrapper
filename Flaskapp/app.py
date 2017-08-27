from flask import Flask, render_template,request,redirect,json
from bs4 import BeautifulSoup
import requests
import sys
import os


app = Flask(__name__,static_url_path='/static')

@app.route('/')
def index():
    return render_template("index.html")
	    
@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    #given_url = 'https://www.yellowpages.ca/search/si/1/Food%20Delivery/toronto'
    given_url = 'https://bulbapedia.bulbagarden.net/wiki/{0}'.format(text)
    #url = 'https://www.newegg.ca/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
    
    #This is how you connect the script with the client site
    open_url = requests.get(given_url)   
    soup = BeautifulSoup(open_url.content, "lxml")
    #image_txt = 'alt = {0}'.format(text)
    try:
        links = soup.find("table", {"class" : "roundy"} , {"style" : "max-width:420px;"})
        name = links.find("big").text
        catogory = links.find("span", {"style" : "color:#000;"}).text
        picture = links.find("img")
        type = links.find("span" , {"style" : "color:#FFF;"}, "b").text


        ablity = links.find_all("table",{"class" : "roundy"},{"style" : "max-width:420px;"})
        table_lists = []
        table_ablity_list = []
        table_field_list = []
        table_otherinfo_list = []

        for abl in ablity:
            yolo = abl.find_all("span",{"style" : "color:#000;"},"Cacophony")
            if yolo:
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
            
        elements = str(picture).split()
        picture_list = []
        
        for ele in elements:
            picture_list.append(ele)
            #print (ele, file=sys.stderr)
            
      
        pic = picture_list[3].replace('"','').replace('src=/', 'http:/')
        
        
        ablity_table_one = []    
        print('hello',file=sys.stderr)
        print ("name: ",name, file=sys.stderr)
        print ("catagorey : ", catogory, file=sys.stderr)
        print ("picture : ", picture, file=sys.stderr)
        print ("type :", type, file=sys.stderr)
        for abl in table_lists2:
            ablity_table_one.append(abl.text.replace('Cacophony',''))
            print("ablity :",abl.text, file=sys.stderr)

        print ("catch rate :", table_otherinfo_list[5], file=sys.stderr)
        print ("egg type : ",table_otherinfo_list[6], file=sys.stderr)
        
        return render_template("poke.html",name=name,catogory=catogory,pic=pic,type = type, catrate = table_otherinfo_list[5],egg = table_otherinfo_list[6],ablity = ablity_table_one)
    except:
        return render_template("error.html")
        
@app.route('/about')
def about():
    return render_template("about.html")        
        
if __name__ == "__main__":
    app.run() 