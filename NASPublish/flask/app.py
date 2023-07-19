# 라이브러리 임포트
# Flask Framework
# view페이지 렌더링을 위한 render_template 메서드
# 요청 데이터에 접근 할 수 있는 flask.request 모듈
# dictionary를 json형식의 응답 데이터를 내보낼 수 있는 jsonify 메서드
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# [POST-3] MongoDB사용을 위한 pymongo와 certifi 임포트
# MongoDB(Atlas Cloud)를 사용하기 위한 pymongo 임포트
from pymongo import MongoClient
import certifi
# [POST-4] DB 커넥션 구성
ca = certifi.where()
client = MongoClient('mongodb+srv://ohnyong:test@cluster0.lu7mz8j.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

# [Ranking GET-2] 웹 크롤링을 위한 임포트
# 크롤링 = 웹페이지에서 어떤 데이터를 가져오는것
import requests
from bs4 import BeautifulSoup

# [Ranking GET-3] 웹 크롤링 URL 지정과 requests를통한 데이터 가져오기->bs를 통한 파싱
URL = "https://kworb.net/spotify/country/us_daily.html"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# "localhost:5001/" URL요청에 메인 뷰 페이지 반환 응답
@app.route('/')
def home():
   return render_template('index.html')

# [POST-0] CREATE 부분부터 코드를 작성하는 것(==POST)이 확인이 가능(READ부터하면 데이터가없어서 테스트 어려움)
# fetch('URL')부분, 반환값은 res로 전달.
# "localhost:5001/guestbook" URL POST방식 요청에 응답
@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    # [POST-1] 프론트로부터 무엇을 받아야 하는가? -> 프론트 input으로부터 name, comment를 받을 것이다.
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    print(name_receive, comment_receive)
    # [POST-2] 클라이언트로부터 받은 데이터를 DB에 넣자 MongoDB연결을 위한 임포트부터 시작(더블체크)
    # [POST-5] DB연결이 완료되었으니 Dictionary key:value형태 데이터들을 doc=리스트 객체에 담는다.
    # INSERT_ONE
    # 저장 - 예시
    # doc = {'name':'bobby','age':21}
    doc = {
        'name' : name_receive,
        'comment' : comment_receive
    }
    # [POST-6] doc에 담았으니 DB에 insert 한다.
    db.fan.insert_one(doc)
    # [POST-7] insert가 완료되었으니 완료 메시지를 반환한다.
    return jsonify({'msg': 'POST 연결 완료!'+'DB 저장 완료!'})

# [GET-0] CREATE 부분이 테스트 완료되어 DB에 자료가 추가되는 상황, READ로 View 페이지에 DB 데이터를 가져와서 보여주자.
# fetch('URL')부분, 반환값은 res로 전달.
# "localhost:5001/guestbook" URL GET방식 요청에 응답
@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    # [GET-1] 필요한 데이터는? -> DB에서 API 데이터를 가져와야 한다.
    all_comments = list(db.fan.find({},{'_id':False}))
    # [GET-2] 가져온 데이터는? -> json으로 변환하여 반환 -> 프론트(js)로 이동
    return jsonify({'result': all_comments})

# [Ranking GET-0] /ranking URL에서 GET 방식으로 요청에 대한 반환 데이터를 작성
# fetch('URL')부분, 반환값은 res로 전달.
# "localhost:5001/ranking" URL GET방식 요청에 응답
@app.route("/ranking", methods=["GET"])
def ranking_get():
    # [Ranking GET-1] 웹 크롤링을 위한 임포트부터 시작한다. 맨위로
    # 위 링크 페이지의 전체 HTML이 아웃풋 된다
    # print(soup)

    # [Ranking GET-4] 특정 텍스트로 원하는 범위 만큼의 HTML소스 가져오기(CLASS, ID가 지정안되서 해당 방법 사용)
    # BeautifulSoup 라이브러리는 엄청 많은 HTML 코드 중에 우리가 원하는 특정 부분 을 빠르고 쉽게 필터링 해주는 라이브러리이다.
    # 원하는 데이터만 추출해보자
    target = "Super Shy"
    # 테스트 코드에서 정리된 원하는 데이터 위치
    e = soup.find(string=target).parent.parent.parent.parent
    print(e)

    # title tr>td중에 text mp라는 클래스td 안에 데이터가 있는데 내부에 데이터들이 있는 자식 태그 경로가 상이하다.

    # [Ranking GET-5] 원하는 범위의 HTML소스에서 원하는 요소 선택 및 변수에 담기
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

    # [Ranking GET-6] 원하는 값을 반환 시켜 주기
    # 이 값들을 rankresult에 담아서 프론트로 반환시켜 보내주자.
    rankingdoc = {
        'artist' : artist,
        'title' : title,
        'rank' : rank,
        'rankdiffer' : rankdiffer
    }
    return jsonify({'rankingresult': rankingdoc})

# app이라는 메인 함수 
# if __name__ == "__main__" 의 의미는 메인 함수의 선언, 시작을 의미
# 이 파이썬 스크립트가 직접 실행될 때에는 main() 함수를 실행하라
if __name__ == '__main__':
	app.run(host='0.0.0.0')
