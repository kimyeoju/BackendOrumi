// 논리 연산자(&&, ||, !)

let x = true; // 1
let y = false; // 0

// &&는 곱
// ||는 합
// ! 는 부정

x && y;
x || y;
!y; // true
!x; // false
// 실무에서 많이 사용
!!y; // !!는 true not*not이니깡
!!"hello"; // hello 출력

!!NaN; // false
!!null; // false
!!undefined; // false

!![]; // true // 이렇게 사용하지 마시고
Number.isNaN({});
Number.isNaN([]);
// 와 object의 길이를 함께 판단하시면 됩니다.

////
// javascript에서는 아래와 같은 단락평가를 자주 사용합니다.

null && y; // false니까 값은 null로 가진다
"world" && "hello"; // 'hello'가 나옴 // 뒤에까지 봐서 그럼

// 단락 평가는 거의 ||를 사용한다!

// let name = ''
// name = name || '이름이 입력되지 않음' -> 이건 '이름이 입력되지 않음'출력

let name = "yeoju";
name = name || "이름이 입력되지 않음"; // yeoju 출력

// 보통은 3항 연산자 + 단락평가로 사용한다.
let 로그인여부 = true;
로그인페이지 = 로그인여부 && "<h1>환영합니다 고객님</h1>";
로그인페이지;

let pw = "";
pw = pw || "패스워드가 입력되지 않았습니다.";
