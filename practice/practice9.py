# print list of articles from url

from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
print("This is a list of article headlines:")
for link in soup.find_all('div', class_='css-xdandi'):
    print(link.text)
print("That's the end of the article headlines!")