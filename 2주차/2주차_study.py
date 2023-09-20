import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time
from konlpy.tag import Komoran
### 구글 뉴스 제목 크롤링
dr = webdriver.Chrome()
url = 'https://news.google.com/home?hl=ko&gl=KR&ceid=KR:ko'
dr.get(url)
time.sleep(5)
news_list=[]
title = dr.find_elements(By.XPATH,"//h4")
for i in title:
    news_list.append(i.text)
news = "\n".join(news_list)
##################

pattern = r'\([^)]*\)'  # () 제거
news = re.sub(pattern=pattern, repl='', string=news)

pattern = r'\[[^\]]*\]'  # [] 내부 내용 제거
news = re.sub(pattern=pattern, repl='', string=news) 

news  = news.replace('...', ' ') #... 제거
    
pattern = r'[^a-zA-Z가-힣]' #특수 문자 제거
news = re.sub(pattern=pattern, repl=' ', string=news)

pattern = r'\b(?:SBS|MBC|KBS|JTBC|연합)\s*뉴스\b' 
news = re.sub(pattern=pattern, repl=" ", string=news)

pattern = r'\b(?:SBS|MBC|KBS|JTBC|연합)\s*News\b' 
news = re.sub(pattern=pattern, repl=" ", string=news)

pattern = r'\b(?:SBS|MBC|KBS|JTBC|연합)\b'
news = re.sub(pattern=pattern, repl=" ", string=news)

##############
komoran = Komoran(userdic="user.dic")
komoran_tag = komoran.pos(news)

words = [word for word, pos in komoran_tag if pos == 'NNP' or pos == 'SL']

#print(komoran_tag)
print(words)
#print(news)

