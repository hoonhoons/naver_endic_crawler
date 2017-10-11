import requests
from bs4 import BeautifulSoup

print("검색하려는 영어 단어를 입력하세요.")
word = input()

url = "http://endic.naver.com/search.nhn?query=" + word
response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")

result = ""
try:
    result += soup.find('dl', {'class':'list_e2'}).find('dd').find('span', {'class':'fnt_k05'}).get_text()
except:
    result = "네이버 사전에 등재되어 있지 않습니다."
print(result)
