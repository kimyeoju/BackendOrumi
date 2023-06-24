# 유용한 순회 가능 객체
# 1) 
# def 곱하기둘(x):
#     return x * 2

# print(list(map(곱하기둘,'123')))
# # ['11','22','33']

# 2)
# def 함수(x):
#     return x > 5
# print(list(filter(함수, range(10))))
# # [6,7,8,9]

# class 문제

# 1)
# class Car(object):
# 	kinds = []
# 	# 클래스 변수
# 	MaxSpeed = 300
# 	MaxPeople = 5
# 	def move(self, x):
# 		print(x, '의 스피드로 움직이고 있습니다.')
# 	def stop(self):
# 		print('멈췄습니다.')

# k5 = Car()
# Car.kinds.append('k5')
# k3 = Car()
# Car.kinds.append('k3')

# print(k5.kinds)
# print(k3.kinds)

# 2)
# class Car(object):
# 	kinds = []
# 	speed = 300
# 	def add_kinds(self, name):
# 		self.kinds.append(name)
# 	def change_speed(self, speed):
# 		self.speed = speed

# k5 = Car()
# k3 = Car()
# k5.add_kinds('k5')
# k3.add_kinds('k3')
# k5.change_speed(500)
# k3.change_speed(250)

# print('k5.kinds:', k5.kinds)
# print('k3.kinds:', k3.kinds)
# print('k5.speed:', k5.speed)
# print('k3.speed:', k3.speed)

# 3)
# class Car(object):
#     MaxSpeed = 300
#     MaxPeople = 5
    
#     def __init__(self, name):
#         self.name = name
    
#     def move(self, x):
#         print(self.name, x, '의 스피드로 움직이고 있습니다.')
        
#     def stop(self):
#         print('멈췄습니다.')

# k5 = Car('케이파이브')
# k3 = Car('케이쓰리')

# k5.move(100)
# k3.move(200)
# k5.stop()

# 4)
class Car(object):
    kinds = []
    MaxSpeed = 300
    MaxPeoeple = 5
    def __init__(self, 이름):
        self.name = 이름
        self.kinds.append(이름)
    def __add__(self, obj):#obj : 더할 요소
				# 더하기를 정의하고 있는 기본 매직메서드
        return 'hello world'
    def move(self, x):
        print(self.name, x, '의 스피드로 움직이고 있습니다.')
        print(self.kinds)
        self.stop()
    def stop(self):
        print('멈췄습니다.')

k5 = Car('케이파이브')
k3 = Car('케이쓰리')

k5.move(100)
k3.move(200)
print(k5 + k3)