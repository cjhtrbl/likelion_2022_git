document.querySelectorAll('.list')[0].addEventListener("click", function(e){
    tabBtn(e.target.dataset.id);
});


function tanBtn(a){
    document.querySelectorAll('.tab-button')[0].addEventListener("click", function(){
        for (let i = 0; i < document.querySelectorAll(".tab-button").length; i++){
            document.querySelectorAll(".tab-button")[i].classList.remove("here");
            document.querySelectorAll(".tab-content")[i].classList.remove("show");
        }
         document.querySelectorAll(".tab-button")[0].classList.add("here");
         document.querySelectorAll(".tab-button")[0].classList.add("show");
     });
}


//아래 코드를 for문으로 변경하기
// document.querySelectorAll('.tab-button')[0].addEventListener("click", function(){
//     document.querySelectorAll('tab-button')[0].classList.remove("here");
//     document.querySelectorAll('tab-button')[1].classList.remove("here");
//     document.querySelectorAll('tab-button')[2].classList.remove("here");
//     document.querySelectorAll('tab-content')[0].classList.remove("show");
//     document.querySelectorAll('tab-content')[1].classList.remove("show");
//     document.querySelectorAll('tab-content')[2].classList.remove("show");
//     document.querySelectorAll(".tab-button")[0].classList.add("here");
//     document.querySelectorAll(".tab-button")[0].classList.add("show");
// });

// document.querySelectorAll('.tab-button')[0].addEventListener("click", function(){
//    for (let i = 0; i < document.querySelectorAll(".tab-button").length; i++){
//        document.querySelectorAll(".tab-button")[i].classList.remove("here");
//        document.querySelectorAll(".tab-content")[i].classList.remove("show");
//    }
//     document.querySelectorAll(".tab-button")[0].classList.add("here");
//     document.querySelectorAll(".tab-button")[0].classList.add("show");
// });