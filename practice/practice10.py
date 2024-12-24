# print out full article from url

from bs4 import BeautifulSoup
import requests

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
print("This is the full article:")
for link in soup.find_all('div', class_='body__inner-container') + soup.find_all('p', class_='paywall'):
    print(link.text)

print("That's the end of the article!")