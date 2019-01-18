import requests
from bs4 import BeautifulSoup


#1. 요청 보낼 url을 저장한다.
url = "https://finance.naver.com/sise/"

#2. 해당 url로 요청을 보낸다.
response = requests.get(url).text #text를 붙이면 편해
#response의 타입은 str
#requests.get(url).json() 어쨌든 뒤에 붙이면 편해짐

#3. 받은 html 파일을 파이썬으로 찾기 편하도록 bs4를 사용한다.
html = BeautifulSoup(response, 'html.parser') #html의 타입은 BeautifulSoup이됩니다.

#4. 선택자를 이용해서 값을 골라낸다. (kospi 지수)
kospi = html.select_one('#KOSPI_now') #id=KOSPI_now 이기 때문에.
#print(kospi.text) == 수치가 나옴.
