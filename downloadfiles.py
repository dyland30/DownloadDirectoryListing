from sys import base_prefix
import requests
import os
from bs4 import BeautifulSoup

def main():
    baseUrl = "<URL>"
    if not os.path.exists("web.html"):
        print("get links")
        page = requests.get(baseUrl)
        if page.status_code == 200:
            file = open("web.html","w")
            file.write(page.content.decode())
            file.close()
    
    if not os.path.exists("links.txt"):
        print("extract links")
        file = open("web.html","r")
        content = file.read()
        file.close()
        soup = BeautifulSoup(content, "lxml")
        vinculos = soup.find_all("a")
        hrefs = []
        linkFile = open("links.txt","w")
        #optional, check for specific file extension
        for v in vinculos:
            if ".jpg" in v["href"].lower():
                hrefs.append(v["href"].lower()+"\n")

        linkFile.writelines(hrefs)
        linkFile.close()

    linkFile = open("links.txt","r")
    linkLines = linkFile.readlines()
    linkFile.close()
    cont = 0
    for li in linkLines:
        cont += 1
        url = baseUrl+li.replace("\n","")
        print(str(cont)+"| " +url)
        #descargar archivos
        rf = requests.get(url)

        ruta = "pictures"+li.replace("\n","")
        open(ruta,"wb").write(rf.content)

    



if __name__ == "__main__":
    main()
    