import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

#url , 지정 정보
url = "https://www.goodprice.go.kr/search/goodstore.do"
data={"OptSido":"14", "OptGugun":"구미시"}

#드라이버 지정
dr = webdriver.Chrome()
dr.get(url)

#request(POST)
res = requests.post(url, data)

#soup
soup = BeautifulSoup(res.content, "html.parser")

#crwling
actor_list = soup.find_all("td", {'class':["board_seven"]})


if res.status_code == 200:

    print(actor_list)
else :
    print("오류 코드 :", res.status_code)