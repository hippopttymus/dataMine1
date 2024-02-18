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