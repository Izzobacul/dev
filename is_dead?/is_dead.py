#This code tells you if someone is dead, based on their wikipedia page.
#The function takes the person's name as an argument
# Optionally, you can pass the language in which you want to search it
# I know, it's dark... 

#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import sys


def is_dead(p, **kwargs):
    lang = kwargs.get('lang', None)
    if len(p.split(" "))>=2:
        p = "_".join([n.capitalize() for n in p.split(" ")])
    link = f"https://{lang}.wikipedia.org/wiki/{p}" if lang else f"https://en.wikipedia.org/wiki/{p}"
    
    r = requests.get(link)
    #Returns -1 if page doesn't exist
    if "Wikipedia does not have an article with this exact name." in r.text:
        return(-1)
    html = BeautifulSoup(r.text, features="html.parser")
    infobox = str(html.findAll("table", {"class": "infobox vcard"}))
    infobox2 = str(html.findAll("table", {"class": "infobox biography vcard"}))
    dead = "Died" in infobox or "Died" in infobox2
    #Returns True/False
    return(dead)

def main():
    p = sys.argv[1]
    lang = None
    if len(sys.argv)>=3:
        lang = sys.argv[2]
    dead = is_dead(p, lang=lang)
    if dead==-1:
        print(f"{p} does not have a Wikipedia page to get the information")
    elif dead == True:
        print(f"Sadly, {p} is dead")        
    else:
        print(f"{p} is very alive!")



if __name__=='__main__':
    main()
