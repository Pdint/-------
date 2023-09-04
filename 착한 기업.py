import requests
from bs4 import BeautifulSoup

#url , 지정 정보
url = "https://www.goodprice.go.kr/search/goodstore.do"
data={"OptSido":"14", "OptGugun":"구미시"}

#request(POST)
res = requests.post(url, data)

#soup
soup = BeautifulSoup(res.content, "html.parser")

#crwling
actor_list = soup.find_all("td", {'class':["board_seven"]})

print(actor_list)