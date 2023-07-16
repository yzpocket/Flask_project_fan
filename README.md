# Flask_project_fan
[Flask] Flask framework 미니프로젝트(project fan) 

## 🖥️ 프로젝트 소개 
뉴진스 아이돌 그룹의 응원댓글을 기록하는 팬사이트 컨셉의 간단한 메모 게시판 형태의 웹 페이지 서비스

## 🕰️ 개발 기간
* 23.07.16일 - 23.07.18일

### 🧑‍🤝‍🧑 맴버구성 
 - 김인용 - 싱글 프로젝트

### ⚙️ 개발 환경 
- **MainLanguage** : `PYTHON`
- **IDE** : VisualStudio Code 1.79.2 (Universal)
- **Framework** : Flask Framework
- **Database** : MongoDB(5.0.11)
- **SERVER** : Flask

## 📌 주요 기능
#### View 구성
* top부분 :<br>
    - 웹 페이지 정보 타이틀(title)
    - 서울시 실시간 기온 표시
    - 글로벌 히트곡 Super Shy의 Spotify 일간 순위
* content부분 : <br>
    1. 응원댓글 기록 : <br>
    - div(#mypost)내 input(#name)의 입력필드 생성 placeholder로 입력 내용 가이드 "닉네임"
    - div(#mypost)내 textarea(#comment)의 입력필드 생성 placeholder로 입력 내용 가이드 "Leave a comment here"
    - 댓글남기기 버튼 save_comment() onclick 이벤트 넣어두기<br>
    2. 응원 댓글 리스트 목록 : <br>
    - 기록(DB)을 불러와서 기록하기 하단 새로운 div에 1행씩 출력되도록 함<br>
* footer부분 :<br>
    - 구성 없음

#### 서울시 실시간 날씨 OpenAPI 사용
- URL로부터 OpenAPI 요청, 기온 부분을 받아와서 출력

#### 웹 크롤링
- URL로부터 Super Shy의 데일리 랭킹 크롤링(soup.select_one)

#### 응원 댓글 기록 진행
- input,textarea에 값 입력
- '댓글남기기' 버튼으로 입력값 DB로 전송 및 저장 (insert)

#### 응원 댓글 목록 확인
- DB에 저장된 기록된 응원 댓글 데이터 받기(find(==read))
- 받은 데이터를 content 부분에 한줄씩 출력