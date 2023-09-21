import selenium
from wordcloud import WordCloud
from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import Counter
import re
import time
from konlpy.tag import Komoran
import matplotlib.pyplot as plt

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

pattern = r'\b(?:SBS|MBC|KBS|JTBC|연합|뉴스A)\b'
news = re.sub(pattern=pattern, repl=" ", string=news)

##############
komoran = Komoran()
komoran_tag = komoran.pos(news)

words = [word for word, pos in komoran_tag if (pos == 'NNP' or pos == 'SL') and len(word) > 1]
c = Counter(words)

wc = WordCloud(font_path='gulim', width=400, height=400, scale=2.0, max_font_size=250)
gen = wc.generate_from_frequencies(c)
plt.figure()
plt.imshow(gen)

wc.to_file('워드클라우드.png')