# 크롤링 = 웹페이지에서 어떤 데이터를 가져오는것

import requests
from bs4 import BeautifulSoup

URL = "https://kworb.net/spotify/country/us_daily.html"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# 위 링크 페이지의 전체 HTML이 아웃풋 된다
# print(soup)

# BeautifulSoup 라이브러리는 엄청 많은 HTML 코드 중에 우리가 원하는 특정 부분 을 빠르고 쉽게 필터링 해주는 라이브러리이다.
# 원하는 데이터만 추출해보자
target = "Super Shy"
# a = soup.find(string=target)
# print(a)
# b = soup.find(string=target).parent
# print(b)
# c = soup.find(string=target).parent.parent
# print(c)
# d = soup.find(string=target).parent.parent.parent
# print(d)
e = soup.find(string=target).parent.parent.parent.parent
print(e)

# title tr>td중에 text mp라는 클래스td 안에 데이터가 있는데 내부에 데이터들이 있는 자식 태그 경로가 상이하다.

# 순위 rank변수에 담는다. tr>td의 첫번째 요소이다.
# 순위변동 rankdiffer변수에 담는다. tr>td의 두번째 요소이다.
rank = e.select_one('tr > td:first-child').text.strip()
rankdiffer = e.select_one('tr > td:nth-child(2)').text.strip()

# a태그는 2~3개인 경우가 있다. nth-child로 정리하려했으나 가끔 두번째 a태그에 제목이 겹치는 데이터가 있었다.
# 따라서, 첫번째가 가수, 마지막(2개인 경우엔 2번째, 3개인 경우 3번째)에 노래 제목인 규칙을 보고
# first-child에 가수, last-child에 노래 제목인 것으로 정리했다.
artist = e.select_one('td.text.mp > div > a:first-child').text.strip()
title = e.select_one('td.text.mp > div > a:last-child').text.strip()

# 변수에 담긴것이 정확한지 콘솔로 확인해본다.
print("Rank : "+rank+"\t", "DIFF : "+rankdiffer+"\n","Artist : "+artist+"\n", "Title : "+title)

# # 오답 노트 (차트 전체를 가져온 케이스)
# # 상위 계층인 tbody은 "차트"이다.
# # 실제 데이터(한곡, 한곡들)들 은 tr에 있다. 우선 tr"들" 전체를 trs라고 변수에 담는다.
# trs = soup.select('#spotifydaily > tbody > tr')
# print(trs)

# # 반복문으로 trs를 돌면서 [rank, rankdiffer, artist, title 변수를 담는다] 를 반복(어디까지? trs 리스트의 끝까지==0부터 전체)
# for td in trs:
# # 양옆 공백을 제거(strip)한 텍스트를 추출하고자 한다. 데이터가 깔끔해서 slice기능을 사용할 필요는 없었다.
# # title tr>td중에 text mp라는 클래스td 안에 데이터가 있는데 내부에 tr>td>div>a태그까지 넘어가야 실질적인 데이터가 있다.
# # rank변수에 담는다. tr>td의 첫번째 요소이므로 first-child를 사용했다.
#     rank = td.select_one('td:first-child').text.strip()
#     rankdiffer = td.select_one('td:nth-child(2)').text.strip()
# # 또한 a태그는 2~3개인 경우가 있다. nth-child로 정리하려했으나 가끔 두번째 a태그에 제목이 겹치는 데이터가 있었다.
# # 따라서, 첫번째가 가수, 마지막(2개인 경우엔 2번째, 3개인 경우 3번째)에 노래 제목인 규칙을 보고
# # first-child에 가수, last-child에 노래 제목인 것으로 정리했다.
#     artist = td.select_one('td.text.mp > div > a:first-child').text.strip()
#     title = td.select_one('td.text.mp > div > a:last-child').text.strip()
# # 변수에 담긴것이 정확한지 콘솔로 확인해본다.
#     print("Rank : "+rank+"\t", "DIFF : "+rankdiffer+"\n","Artist : "+artist+"\n", "Title : "+title)

