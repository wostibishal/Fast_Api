import requests 
from bs4 import BeautifulSoup 
fast = requests.get('https://fastapi.tiangolo.com/')
soup = BeautifulSoup(fast.content, 'html.parser')
print(soup.prettify())