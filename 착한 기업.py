import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#url , 지정 정보
url = "https://www.goodprice.go.kr/search/goodstore.do"
data={"OptSido":"14", "OptGugun":"구미시"}

#드라이버 지정
dr = webdriver.Chrome()
dr.get(url)

# 데이터를 POST 방식으로 서버에 전송할 수 있는 웹 페이지로 이동합니다.
dr = webdriver.Chrome()
dr.get(url)

# 데이터 입력
opt_sido = dr.find_element(By.NAME, "OptSido")
opt_gugun = dr.find_element(By.NAME, "OptGugun")

opt_sido.send_keys("14")  # 시도 입력
opt_gugun.send_keys("구미시")  # 구군 입력

# 데이터 전송 (폼 제출)
opt_gugun.send_keys(Keys.RETURN)


#request(POST)
res = requests.post(url, data)

#soup
soup = BeautifulSoup(res.content, "html.parser")
#클래스 요소 클릭하기


num = 4
for i in range(5):
    elements = dr.find_elements (By.XPATH, '//*[@id="cont-sbj"]/form[2]/div[2]/a[' + str(num) + ']')
    for element in elements:
        element.click()
        num += 1

        time.sleep(10)

#crwling
actor_list = soup.find_all("td")


if res.status_code == 200:

    with open("all.txt", "a", encoding="utf-8") as file:
       for actor in actor_list:
            file.write(str(actor) + "\n")

else :
    print("오류 코드 :", res.status_code)