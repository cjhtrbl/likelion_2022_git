//EventTarget.addEventListener('eventType', function, useCapture)

//눌러봐
document.getElementById("btn").addEventListener("click", function() {
    console.log("click!!!!!");
});

//숫자
var num = 0;
document.getElementById('plus').addEventListener("click",function() {
    num++;
    document.getElementById('num').innerHTML = num;
});

document.getElementById('minus').addEventListener("click",function() {
    num--;
    document.getElementById('num').innerHTML = num;
});

//여기 눌러봐 -> 짠 내가 생겼어
// document.querySelector(".bar").addEventListener("click", function() {
//     document.querySelector(".newBar").style.display = "block";
// });

document.querySelector(".bar").addEventListener("click", function() {
    document.querySelector(".bar").innerHTML = "눌렸어!";
    document.querySelector(".newBar").classList.toggle("show");
});