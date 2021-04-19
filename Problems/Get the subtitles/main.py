import requests

from bs4 import BeautifulSoup

num = int(input())
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
p2 = soup.find_all('h2')
print(p2[num].text)