import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

url = "https://www.goodprice.go.kr/search/goodstore.do" #url , 지정 정보

dr = webdriver.Chrome() #드라이버 지정
dr.get(url)

opt_sido = dr.find_element(By.NAME, "OptSido") # 데이터 입력
opt_sido.send_keys("경상북도")  # 시도 입력

time.sleep(3) #지정 대기

opt_gugun = dr.find_element(By.NAME, "OptGugun")
opt_gugun.send_keys("구미시")  # 구군 입력


search = dr.find_element(By.XPATH, '//*[@id="cont-sbj"]/form[1]/div/div/div/a')
search.click() #검색 클릭

#크롤링 코드
try:
    sectors_list = []
    names_list = []
    items_list = []
    prices_list = []
    call_numbers_list = []
    addresses_list = []
    
    num = 1
    for i in range(5):
        #페이지 넘기는 코드
        elements = dr.find_elements (By.XPATH, '//*[@id="cont-sbj"]/form[2]/div[2]/a[' + str(num) + ']')

        for element in elements:
            element.click()
            sector = dr.find_elements(By.CLASS_NAME, "board_two") #업종
            name = dr.find_elements(By.CLASS_NAME, "board_three") #업소 이름
            item = dr.find_elements(By.CLASS_NAME, "board_four")  #판매 물품
            price = dr.find_elements(By.CLASS_NAME, "board_five") #가격
            call_number = dr.find_elements(By.CLASS_NAME, "board_six") #전화번호
            address = dr.find_elements(By.CLASS_NAME, "board_seven") #주소
            
            sectors_list.extend([sector.text for sector in sector])
            names_list.extend([name.text for name in name])
            items_list.extend([item.text for item in item])
            prices_list.extend([price.text for price in price])
            call_numbers_list.extend([call_number.text for call_number in call_number])
            addresses_list.extend([address.text for address in address])
            
            num += 1
            
            time.sleep(10)

#이거는 잘 되는지 모르겠음.
except TimeoutError:
    print("오류 발생")

sectors_list = [x for x in sectors_list if x != '업종']
names_list = [x for x in names_list if x != '업소명']
items_list = [x for x in items_list if x != '주요품목']
prices_list = [x for x in prices_list if x != '가격']
call_numbers_list = [x for x in call_numbers_list if x != '연락처']
addresses_list = [x for x in addresses_list if x != '주소']

print("Sectors:", sectors_list)
print("Names:", names_list)
print("Items:", items_list)
print("Prices:", prices_list)
print("Call Numbers:", call_numbers_list)
print("Addresses:", addresses_list)
