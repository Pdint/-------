import requests 
res = requests.get("http://naver.com")
print("응답코드 :", res.status_code) #200 이면 정상

#if res.status_code == requests.codes.ok:
#   print("정상")
#else:
#   print("문제 발생 [에러코드 ", res.status_code, " ]")

print(len(res.text))

with open("mtgoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)