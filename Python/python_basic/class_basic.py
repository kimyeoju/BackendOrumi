''' 
Class: 코드를 재사용 -> 함수

계산기

class 틀
Instance 틀로 찍어낸 결과물
Method 클래스 내부의 함수
'''

# result = 0
# result2 = 0

# def add(number):
#     global result
#     result += number
#     return result

# def add2(number):
#     global result2
#     result += number
#     return result

# print(add(1))
# print(add(2))

# print(add2(1))
# print(add2(2))

# 더하기 클래스
class Add(object):
    # 생성자
    # result = 0 # 클래스 변수
    # 근데 클래스 변수는 거의 사용을 안함 
    def __init__(self):
        self.result = 0
        # self는 인스턴스 변수 
        
    def add(self, number):
        self.result += number
        return self.result
    
    def sub(self,number):
        self.result -= number
        return self.result
    
# Add로 만든 결과물(객체, 인스턴스)
'''
Add 
- 인스턴스 (self는 인스턴스이다. 클래스 처음에 딱 생기는 순간)
    result = 0
    def add()
'''

add_func = Add()
add_func2 = Add()

print(add_func.add(10))

# 클래스의 상속 : 상속은 내가 지금 가지고 있는 기능을 변화시키지 않으면서 다른 클래스의 기능을 추가하고 싶을 때 상속을 받는 것이다.
# class Sub

# class Add(Sub)
# sub2

# 메서드 오버라이딩 : 상속 받아온 기능을 재정의해서 쓸 때 
