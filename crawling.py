import requests #requests 모듈 불러오기, 모듈은 함수를 묶어놓은 것
from bs4 import BeautifulSoup #bs4 모듈에서 BeautifulSoup 기능 불러오기
from datetime import datetime #날짜 출력을 위한 모듈

#--------------------
#requests
url = "http://www.daum.net"
response = requests.get(url)
#requests.get(url) : 모듈명.함수이름(재료) - requests 모듈 안의 get 함수가 url을 재료로 server에 요청을 보냄 -> server의 응답값은 requests.response
#requests.get: get 요청을 보내는 기능 (요청은 put, get, post, delete가 있음)
#client: 요청 -> server: 응답 -> client: 응답 받은 값을 활용

print(response.text) #response에서 text를 출력 -> html 코드가 출력됨

#--------------------
#BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser') #BeautifulSoup(데이터, 파싱방법)
#데이터: BeautifulSoup 안에 담을 데이터, html과 x뭐시기...가 올 수 있음

print(soup.title) #response.text에 있는 title tag를 가져옴
print(soup.title.string) #response.text에 있는 title tag 중 문자열(실제 title값)만 출력
print(soup.span) #response.text에 있는 가장 상단의 span tag를 출력
print(soup.findAll('span')) #response.text에 있는 모든 span tag를 출력

#--------------------
#실시간 검색어 추출

#1. daum 사이트의 html파일을 열어 실시간 검색어 데이터가 가지고 있는 공통점 찾기
file = open("daum.html","w") #"daun.html"이라는 파일을 생성
file.write(response.text)
file.close #파일 닫음

#2. 실시간 검색어의 공통점: a태그, class="link_favorsch @n"

#3. html 문서에서 모든 a태그 중 link_favorsch를 가진 것만 추출
results = soup.findAll("a","link_favorsch")

#4. 실시간 검색어 결과를 정리해서 출력
for  result in results:
    print(result.get_text(),"\n")

#5. 날짜 출력
print(datetime.today())

#6. 파일로 출력
#open(파일, 모드)
#모드: r-read-읽기만 가능 / w-write-새로운 내용이 기존 내용을 덮어 씀 / a-append- 기존 내용에 추가
