'''
Dictionary : {'key':'value'}
리스트를 보완하기 위해서 -> 그냥 값들을 나열하게 된다면 리스트를 사용하겠지만, 딕셔너리는 원하는 값에 빠르게 접근하기 위해 생성

1. key, value
2. 순회는 가능 -> for문
    - 키만 순회
    - 값만 순회
    - 키, 값 쌍으로 순회
'''


x = {'a':1, 'b':2}

# 키 x.keys()
# 값 x.values()
# 키,값 x.items()

# for i in x.keys():
# for i in x.values():
# for i,j in x.items():

print(x.keys())
print(x.values()) # ([])
print(x.items()) # 리스트 안의 튜플로 들어 가 있다 ([()])

# enumerate -> 인덱스를 만들어 줄 때

x = {'a':2, 'b':3}
# key, value 모두 순회
for i in x:
    print(i,x[i])
    
for i,j in x.items():
    print(i,j)

# 값만 순회
for i in x.values():
    print(i)
    
# 키만 순회
for i in x:
    print(i)
