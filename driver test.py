import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


#Headless Chrome 사용
#options = webdriver.ChromeOptions()
#options.add_argument('headless')    #적용
#options.add_argument('disable-gpu')     #gpu 사용 x
#options.add_argument('lang=ko_KR')  # 언어 설정

#드라이버 지정
dr = webdriver.Chrome()
dr.get("https://www.goodprice.go.kr/search/goodstore.do")

#태그 확인

for i in range(1, pageNum):

    ame = find_elements_by_class_name('board_three')
    address = find_elements_bt_class_name('board_seven')
    call = find_elements_bt_class_name('board_six')
    goods = find_elements_bt_class_name('board_four')
    prize = find_elements_bt_class_name('board_five')