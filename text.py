import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://www.goodprice.go.kr/search/goodstore.do"

dr = webdriver.Chrome()
dr.get(url)


# 데이터 입력
opt_sido = dr.find_element(By.NAME, "OptSido")
opt_sido.send_keys("경상북도")  # 시도 입력

#적용까지 대기
time.sleep(3)

#wait = WebDriverWait(dr, 10)
#wait.until(EC.presence_of_element_located((By.NAME, "OptGugun")))

opt_gugun = dr.find_element(By.NAME, "OptGugun")
opt_gugun.send_keys("구미시")  # 구군 입력


time.sleep(10)