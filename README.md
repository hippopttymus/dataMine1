This data was scraped using the following scripts from the greatest books .org and good reads best lists using a counter to access adittional pages

import requests
from bs4 import BeautifulSoup
rank = 1
csvStr = ""
URL1 = "https://thegreatestbooks.org/page/"
URL2 = "?_nospa=true"
for number in range(1,101):
    url3 = URL1 + str(number) + URL2
    page = requests.get(url3)

    soup = BeautifulSoup(page.content , "html.parser")
    #print(soup.prettify())
    results = soup.find(class_="list-group-item book-list-item p-0 pt-3")

    #print(results.prettify())

    job_elements = soup.find_all("li", class_="list-group-item book-list-item p-0 pt-3")

    for job_element in job_elements:
        #print(job_element.prettify())
        title_element = job_element.find("a")
        company_element = job_element.find_all("a")
        count = 0
        csvStr += str(rank) + ","
        for x in company_element:
            if(not x.text.isspace()):
                csvStr += x.text
                if(count == 0):
                    csvStr += ","
                    count += 1
        csvStr += "\n"
        rank += 1
    #print(title_element.text)
    #print(company_element[2].text)
print(csvStr)

-------------------------------------------------------------------------
import requests

from bs4 import BeautifulSoup

rank = 1 
csvStr = ""
   
for number in range(1,26):
    
    URL = "https://www.goodreads.com/list/show/1.Best_Books_Ever?page="

    page = requests.get(URL+ str(number))

    soup = BeautifulSoup(page.content , "html.parser")

    #print(soup.prettify())

    itemtype="http://schema.org/Book"

#results = soup.find_all(itemtype="http://schema.org/Book")

#print(results.prettify())

    job_elements = soup.find_all(itemtype="http://schema.org/Book")

    for job_element in job_elements:
        #print(job_element.prettify())
        
        title_element = job_element.find("span", itemprop="name")
        
        
        company_element = job_element.find("div", class_="authorName__container")
      
        
        location_element = job_element.find("span", class_="minirating")
        
        
        csvStr += str(rank) + "," + title_element.text.strip().replace(',', ' ') + "," + company_element.text.strip().replace(',', ' ') + "," + location_element.text.strip().replace(',', ' ') + "\n"
        rank += 1
    
    

print(csvStr)
