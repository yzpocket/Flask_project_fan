$(document).ready(function () {
    set_temp();
    show_comment();
    show_ranking();
    show_date();
});
// [Create]
function save_comment() {
    let formData = new FormData();
    formData.append("sample_give", "샘플데이터");

    fetch('/guestbook', { method: "POST", body: formData }).then((res) => res.json()).then((data) => {
        console.log(data)
        alert(data["msg"]);
    });
}
// [Comment Read]
function show_comment() {
    fetch('/guestbook').then((res) => res.json()).then((data) => {
        console.log(data)
        alert(data["msg"])
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
        alert(data["msg"])
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
