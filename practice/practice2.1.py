# write the result into a text file


from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
file_name = input('Enter name of file: ')


with open(file_name, 'w') as open_file:
    for link in soup.find_all('div', class_='css-xdandi'):
        open_file.write(str(link.text))
