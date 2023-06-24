'''
list -> 배열 : 자료구조

1. 시퀀스형 -> 순서를 가지고 있다(이어져 있다) -> 인덱스
    인덱스 -> 인덱싱, 슬라이싱 -> 인덱스를 이용한 함수 사용이 가능

2. 값 변경이 가능(mutable)


'''
# mutuable 리스트는 값이 같은 곳을 가리킨다 리스트는 값이 변경이 가능하기 때문에 같은 곳을 가리킬때 []에 변경 가능 

x = [1,2]
y = x

y.append(3)

print(y)
print(x)

# immutable 변하지 않기 때문에 '1'을 가르켰던 y가 새롭게 2를 가리켜야함 왜? 숫자는 변하지 않기 때문

x = 1
y = x

y += 1
print(y)
print(x)


1,2,3,4,5

x = 1
y = 1

y = 2


'''
mutuable만 얕은 복사가 일어나기 때문에 mutuable을 잘 알아두면됨 
얕은 복사 
mutable한 객체 안에서 ' = , [:] , object.copy() ' 는 다 얕은 복사다.
복사 -> 메모리 참조
얕은 복사는 복사처럼 보이지만 사실 하나다. 
얕은 복사 -> copy() 같은 id 메모리 할당
깊은 복사 -> deepcopy() 아예 다른 id 메모리 할당 
'''

list1 = [1,2,3,4]
list2 = list1

list1.append(5)
print(id(list1))
print(id(list2))



list3 = [1,2,[3,4]]
list4 = [[3,4],5]

list4.append(6)

print(id(list3[2:3]))
print(id(list4[0:1]))

# 이 아이들은 list안의 list [3,4]를 가리키기 때문에 같은 Id가 나온다

# list1 -> 1,2,3,4,5
# list2 -> 1,2,3,4,5
# list1과 list2는 가리키는 것이 같음 그래서 값이 변경이 되더라도 두 개 다 영향을 받음 
# 복사라기 보단 -> 같은 메모리 참조


# immutable

num1 = 1
num2 = num1
num2 += 1
print(num1)
print(num2)

# 여기서 num1 = 1
# num1 = num2 --> 1 같은 곳을 바라보고 있음 
# num2 +=1
# num2 -> 2 값이 변경 됐기 때문에 새롭게 '2'를 가리키게 된다