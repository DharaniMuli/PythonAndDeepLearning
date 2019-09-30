from bs4 import BeautifulSoup
import requests

def soup_search():
    url= "https://www.umkc.edu/calendar/"
    # url = "https://www.trumba.com/s.aspx?calendar=UMKC&widget=main&srpc.cbid=trumba.spud.4&srpc.get=true"
    response= requests.get(url).text

    soup= BeautifulSoup(response, "lxml")

    # pretty-printing
    print(soup.prettify())




    # table = soup.find("table",{'class':'twSimpleTableTable'})
    #
    # rows = list()
    # for row in table.findAll("tr"):
    #   print(row.prettify())
    #

if __name__== '__main__':
    soup_search()
