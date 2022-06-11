//getElementById('id 값')
document.getElementById('lion').style.color = "red";

//getElementsByTagName('태그 이름')
const animal = document.getElementsByTagName("li");
//tiger의 색 바꾸기
document.getElementsByTagName("li")[1].style.color = "blue";

//getElementsByClassName('class 값')
document.getElementsByClassName('bear')[0].style.color = "green";

//document.querySelector('css선택자')
//document.querySelectorAll('css 선택자')
document.querySelectorAll(".animal")[0].style.color = "pink"

//DOM 조작
//inner html
document.querySelectorAll(".animal")[1].innerHTML = "rabbit";
const animals = document.getElementById("animals");
//리스트에 요소 추가
animals.innerHTML += "<li class = 'animal'>Cat</li>";

//css
//class 추가
document.querySelectorAll(".box")[0].classList.add("purple");
//class 제거
document.querySelectorAll(".box")[0].classList.remove("purple");
//toggle
document.querySelectorAll(".box")[0].classList.toggle("yellow");