import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#url , 지정 정보
url = "https://www.goodprice.go.kr/search/goodstore.do"

#드라이버 지정
dr = webdriver.Chrome()
dr.get(url)

# 데이터 입력
opt_sido = dr.find_element(By.NAME, "OptSido")
opt_sido.send_keys("경상북도")  # 시도 입력

#지정 대기
time.sleep(3)

opt_gugun = dr.find_element(By.NAME, "OptGugun")
opt_gugun.send_keys("구미시")  # 구군 입력

#검색 클릭
search = dr.find_element(By.XPATH, '//*[@id="cont-sbj"]/form[1]/div/div/div/a')
search.click()

#크롤링 코드
try:

    shop_list=[]
    num = 1
    for i in range(5):
        #페이지 넘기는 코드
        elements = dr.find_elements (By.XPATH, '//*[@id="cont-sbj"]/form[2]/div[2]/a[' + str(num) + ']')

        for element in elements:
            element.click()
            # <td> 데이터 전체 찾기
            shop_data = dr.find_elements(By.XPATH, "//td")
            num += 1
            for k in shop_data:
                shop_list.append(k.text)
            #10초간 멈춤
            time.sleep(10)

#이거는 잘 되는지 모르겠음.
except TimeoutError:
    print("오류 발생")
