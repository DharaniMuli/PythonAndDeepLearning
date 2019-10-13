from bs4 import BeautifulSoup
import requests

def soup_search():
    url= "https://scikit-learn.org/stable/modules/clustering.html#clustering"
    response= requests.get(url).text
    soup= BeautifulSoup(response, "html.parser")
    table = soup.find("table",{'class':'docutils'})
    theads = table.find("thead")
    # print(theads)
    for heads in theads:
        headings = theads.find_all('th')
        headings=[ele.text.strip() for ele in headings]
    print(headings)
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        print(cols)

if __name__== '__main__':
    soup_search()
