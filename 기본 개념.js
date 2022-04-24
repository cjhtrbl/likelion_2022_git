/*var: 변수 중복 선언 가능*/
var num = 3;
console.log(num);

var num = 20;
console.log(num);

/*let: 변수 중복 선언 불가능*/
let num = "a";
console.log(num);

/*const: 변수 중복 선언 불가능, 변수에 할당된 데이터 변경 불가능 -> 변수가 아니라 상수라 부름*/
const num = 10;
console.log(num);

/*변수 이름 설정*/
//1. 변수 이름은 카멜케이스 방법으로 작성
let userName = "cjhtrbl"; //(O) 소문자-대문자 순서
let use_name = "cjhtrbl"; //(X) 
//2. 변수 이름은 _, $, 문자로만 시작
//3. 상수나 축약어는 대문자와 스네이크케이스 방식(단어와 단어를 _로 연결)으로 작성
//4. 예약어는 사용할 수 없음


//자료형
//자료형_원시 타입(기본 자료형 또는 기본형)
let number = 1; //숫자형(number)
let str = "abc"; //문자열형(string)
let bool = true; //또는 false, 논리형(boolean)
let undi = undefinced; // undefined
let nul = null; //nul(object)
let symbol = Symbol(); // symbol

console.log(typeof(1)); //자료형 확인

//자료형_참조 타입(참조 자료형 또는 참조형)
let array = []; //배열(object)
let obj = {}; //객체(object)
let func = function(){}; // 함수(function)

//자료형_숫자형
let IsInfinity = 10 /0; //숫자를 0으로 나눔 -> 무한, Infinity
let IsNaN = 10 / "칠"; //숫자를 문자로 나눔 -> 불가능, NaN

let sum = 0.1 + 0.2;
console.log(sum); //숫자는 2진수로 저장되기 때문에 연산결과가 근사치로 나올 가능성이 있음

//자료형_문자열형
let str1 = "abd"; //시작과 끝의 따옴표를 일치
let str2 = 'def';

let str3 = "I'm fine thank you!"; //작은따옴표가 포함되어져 있으면 큰따옴표로 문자열 작성(반대도 동일)
let str4 = "I'm fine thank you! \"and you?\""; //작은따옴표와 큰따옴표가 모두 사용되면 따옴표 앞에 \ 붙여주기

//자료형_undefined
let one; 
console.log(one); //one에 변수가 할당되어 있지 않기 때문에 undefined가 출력

//자료형_null
let two = null; // 명시적으로 변수 공간이 비어있음을 의미할 때 사용
