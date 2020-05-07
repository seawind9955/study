from bs4 import BeautifulSoup
import requests

html = requests.get("http://dygbjy.12371.cn/special/fzdygz/").text()
soup = BeautifulSoup(html, 'lxml')
print(soup.title)