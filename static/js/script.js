$(document).ready(function () {
    set_temp();
    show_comment();
    show_ranking();
    show_date();
});
// [Create]
function save_comment() {
    // index.html로부터 값 가져오기
    let name = $('#name').val()
    let comment = $('#comment').val()
    // formData 객체를 생성하고
    let formData = new FormData();
    // append()통해 {key,value}를 객체에 담는다
    formData.append("name_give", name);
    formData.append("comment_give", comment);
    // POST 요청에 위 formData를 body에 담아 요청한다.
    fetch('/guestbook', { method: "POST", body: formData }).then((res) => res.json()).then((data) => {
        console.log(data)
        alert(data["msg"])
        // 브라우저 새로고침 추가
        window.location.reload();
    });
}
// [Comment Read]
function show_comment() {
    fetch('/guestbook').then((res) => res.json()).then((data) => {
        // json 형식으로 변환, 반환된 데이터가 res 인자로 들어옴
        // res.json()에 의해 Promise 객체로 변환되어 data에 저장
        // data 내용 테스트
        console.log(data)

        // data의 내용이 OpenAPI로부터 데이터 받는것과 동일
        // 리스트 형태의 data를 rows 변수에 담고
        let rows = data['result']
        console.log("rows===>"+rows)

        // 반복문 전에 하드코딩 부분 비워주기
        $('#comment-list').empty();

        // forEach 반복문을 통해
        rows.forEach((a)=>{
            // 리스트에 있는 key의 value들을 각 변수에 담기
            let name = a['name']
            let comment = a['comment']

            console.log("name===>"+name+"\t comment===>"+comment)
            // index.html에 위 변수들이 들어가도록 백틱 내 자리표시자${variable} 작성한 내용을 temp_html에 작성
            let temp_html = `<div class="card">
                                <div class="card-body">
                                    <blockquote class="blockquote mb-0">
                                        <p>${comment}</p>
                                        <footer class="blockquote-footer">${name}</footer>
                                    </blockquote>
                                </div>
                            </div>`
            // 위 temp_html을 index.html의 #comment-list div에 붙여주기.
            $('#comment-list').append(temp_html)
        })
    })
}
// [Temp Read]
function set_temp() {
    fetch("http://spartacodingclub.shop/sparta_api/weather/seoul").then((res) => res.json()).then((data) => {
        console.log(data)
    });
}
// [Ranking Read]
function show_ranking() {
    fetch('/ranking').then((res) => res.json()).then((data) => {
        console.log(data)
        // crawldata라는 리스트 객체 생성(promise인 data객체를 리스트로 변환)
        let crawldata = data['rankingresult']

        // 각 변수에 지정 데이터 담기
        let artist = crawldata['artist']
        let title = crawldata['title']
        let rank = crawldata['rank']
        let rankdiffer = crawldata['rankdiffer']
        console.log(artist,title,rank,rankdiffer)

        // HTML태그(id)에 각 데이터 비우기 후 삽입
        $('#artist').empty().append(artist);
        $('#title').empty().append(title);
        $('#rank').empty().append(rank);
        $('#rankdiff').empty().append(rankdiffer);
    })
}
// [Date Read]
function show_date() {
    let Target = document.getElementById("date");
    let time = new Date();

    let year = time.getFullYear();
    let month = time.getMonth();
    let date = time.getDate();
    let day = time.getDay();
    let week = ['일', '월', '화', '수', '목', '금', '토'];

    // let hours = time.getHours();
    // let minutes = time.getMinutes();
    // let seconds = time.getSeconds();

    Target.innerText =
        `${year}년 ${month + 1}월 ${date}일 ${week[day]}요일 `;
    // `${hours < 10 ? `0${hours}` : hours}:${minutes < 10 ? `0${minutes}` : minutes}:${seconds < 10 ? `0${seconds}` : seconds}`;
}