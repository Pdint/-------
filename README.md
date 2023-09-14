# Crwling-r
착한 가격 업소 리스트와 주소를 수집을 목표 ("https://www.goodprice.go.kr/search/goodstore.do")

참고 사이트
1. https://www.selenium.dev/documentation/webdriver/getting_started/first_script/
2. https://wikidocs.net/
3. https://teamlab.github.io/jekyllDecent/blog/crawling%20with%20python/Selenium%EC%9C%BC%EB%A1%9C-%EB%84%A4%EC%9D%B4%EB%B2%84-%EC%97%B0%EA%B7%B9-%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%81%AC%EB%A1%A4%EB%A7%81%ED%95%98%EA%B8%B0-with-Python
4. https://overface.tistory.com/567
5. https://rednooby.tistory.com/98

처음에는 beautifulsoup를 이용하여서 크롤링을 시도했으나 동적 사이트여서 selenium 페키지를 이용해서 크롤링을 시도하였음.
res = requests.post(url, data) -> 현재 try: 이후 코드

총 shop_data.txt에 정보를 적어놓았고 크롤링을 사용했다.
