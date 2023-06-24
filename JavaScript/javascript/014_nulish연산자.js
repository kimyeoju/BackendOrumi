// https://ko.javascript.info/nullish-coalescing-operator
// 나온지 얼마되지 않았기 때문에 선임이 모를 수 있다.

// 중간에 하나라도 값이 들어있다면 그 값을 출력한다.
let firstname = null;
let lastname = null;
let nickname = null;

firstname ?? lastname ?? nickname ?? "익명의 사용자";

// 출력 - 익명의 사용자

// 중간에 하나라도 값이 들어있다면 그 값을 출력한다.
// let firstname = null;
// let lastname = null;
// let nickname = 'licat';

// firstname ?? lastname ?? nickname ?? '익명의 사용자'

// 출력 - licat

let a = null;
let b = 10;
let c = null;
a ?? 100; // if null이냐? 그렇다면 100을 넣겠다
a ?? b;
a ?? b ?? c; // => (a ?? b) ?? c

//nullish 연산자와 단락평가의 차이점
let height = 0;
height || 100; // 100
height ?? 100; // 0출력 height가 null이 아니기 때문에 숫자이기 때문에 0 출력

//// 제일 중요한건 ||, ?? null or undefined일땐 값이 있는 값을 출력
// || : 0, null, undefined를 false로 판단
// ?? : null, undefined를 false로 판단 // ??는 0을 false로 판단하지 않음

// ??와 ||의 차이
// ||는 첫 번째 truthy 값 반환
// ??는 첫 번째 정의된(defined) 값 반환

let test = 0;

console.log(test || 10000); // 10000
console.log(test ?? 10000); // 0
