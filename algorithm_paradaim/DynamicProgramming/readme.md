최적부분구조와 중복되는 부분구조 두가지로 대별됨

## 1. 최적 부분구조

- 최적부분구조가 있다는것은, "부분 문제들의 최적의 답을 이용해서, 기존 문제의 최적의 답을 구할 수있다는 것"


- 예 : 피보나치 수열, 서울에서 부산까지의 최단거리
> ![스크린샷 2023-10-19 오후 7.56.05.png](algorithm_paradaim/DynamicProgramming/image/스크린샷 2023-10-19 오후 7.56.05.png)
> 서울에서 H,I,J 로가는 최단경로를 풀어야함
> 이 상황에서 각각 4,6,8 더한것을 비교하면 서울에서 부산까지 최적거리 알 수있음


## 2. 중복되는 부분문제

- 피보나치 예시
> 5를 해결위해서는 4,3 을해결하고....그런데 중복되는 문제 3,2,1 이 있음 
> **중복되는 부분문제**


- 합병정렬의 경우
> ![스크린샷 2023-10-19 오후 7.57.57.png](..%2F..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fty%2Fy6_xq5fs3wng_7n74vfny27m0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_aBYBj6%2F%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202023-10-19%20%EC%98%A4%ED%9B%84%207.57.57.png)
> 왼쪽 오른쪽 해결은 완전히 독립적임
> 이것은 결국 **중복되지 않는 부분문제**임

## 3. Danamic programming

- 최적 부분구조가 있다 -> 기존문제를 부분문제로 나눠서 풀 수 있다. -> 중복되는 부분 문제들이 있을 수있다
> 비효율이 있을 수있음 
> 그런데 이런 비효율을 해결위한것이 DP임
> ![스크린샷 2023-10-19 오후 8.00.35.png](..%2F..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fty%2Fy6_xq5fs3wng_7n74vfny27m0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_4biFX7%2F%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202023-10-19%20%EC%98%A4%ED%9B%84%208.00.35.png)
> 정리하면 DP는 이럴때 해결하는 것

- DP 란
> 한 번 계산한 결과를 **재활용하는 방식**
> ![스크린샷 2023-10-19 오후 8.01.26.png](..%2F..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fty%2Fy6_xq5fs3wng_7n74vfny27m0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_UxCGQa%2F%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202023-10-19%20%EC%98%A4%ED%9B%84%208.01.26.png)
> ```fib(7)``` 을 풀기위한 중복문제가 많음
> 이 중복을 한번씩만 딱 풀자는게 그 취지임 

- DP 구현 방법은 2가지임
> 1. Memorization
> 2. Tabulation

## 4. Memoization

- 카페 알바때 커피,케익,와플 같이 많이 시키는데, 매번 때마다 하기 번거로워 그래서 하나로 묶자 -> 메모
- *중복되는 계산은 한번만 계산 후 메모* -> 메모리제이션

- 피보나치수열에서!
> 보통 다시 쓸 값을 cache 라고함
> 
> fib(2) 는 base case 이므로 곧바로 답을 알 수 있음
> ![스크린샷 2023-10-19 오후 8.15.29.png](..%2F..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fty%2Fy6_xq5fs3wng_7n74vfny27m0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_B9wWPu%2F%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202023-10-19%20%EC%98%A4%ED%9B%84%208.15.29.png)
> 메모라이제이션으로 DP로 중복되는 부분문제의 중복되는 비효율성 해결함


## 5. 피보나치 수열
> 실습 설명
> 
> 
> n 번째 피보나치 수를 찾아주는 함수 fib_memo을 작성해 보세요.
> fib_memo는 꼭 memoization 방식으로 구현하셔야 합니다!
> 

> - 힌트 1
> Memoization 방식으로 문제를 풀면 재귀 함수를 사용하는데요. 재귀 함수를 작성할 때 가장 먼저 생각해야 하는 두 가지가 무엇인지 기억하시나요?

> - 힌트 2
> 재귀 함수를 작성할 때에는 base case와 recursive case에 대해 생각해야 합니다.
> - Recursive case: 현 문제가 너무 커서, 같은 형태의 더 작은 부분 문제를 재귀적으로 푸는 경우
> - Base case: 이미 문제가 충분히 작아서, 더 작은 부분 문제로 나누지 않고도 바로 답을 알 수 있는 경우
우선 base case가 무엇인지 생각해 볼까요?


> - 힌트 3
> - Recursive case에는 두 가지 경우가 있습니다.
> - fib_memo(n, cache)를 호출했다고 가정했을 때…
> - 이미 n 번째 피보나치 수를 계산한 경우, 즉 cache[n]이 존재하는 경우
> - 아직 n 번째 피보나치 수를 계산하지 않은 경우, 즉 cache[n]이 존재하지 않는 경우
두 경우를 고려해서 코드를 작성해 보세요.







