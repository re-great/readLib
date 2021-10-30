import json

from bs4 import BeautifulSoup
import requests


# Function to get required url where scraping has to be to done
def get_flipkart_url(self):
    query_parsed = "%20".join(self.split(" "))
    search_url = (
        f"https://www.flipkart.com/books/pr?sid=bks&q={query_parsed}&otracker=categorytree"
    )
    return search_url


s = input("Enter the book you want to scrape ")
# Request library to get source_code of page
fp = requests.get(get_flipkart_url(s))
content = fp.content
# parsing using bs4
soup = BeautifulSoup(content, 'lxml')
# Dict is dictionary of result that we have to return
# scraping codes
Dict = {}
books = soup.find_all('div', class_='_4ddWXP')
for i in range(len(books)):
    dt = {}
    Title = books[i].find('a', class_='s1Q9rs')['title']
    Link = 'https://www.flipkart.com' + books[i].find('a', class_='s1Q9rs')['href']
    price = books[i].find('div', '_30jeq3').text
    detail = books[i].find('div', '_3Djpdu').text
    dt['Title : '] = Title
    dt['Link : '] = Link
    dt['Price : '] = price
    dt['Detail : '] = detail
    Dict[i] = dt
# printing dict
print(json.dumps(Dict, indent=2))
