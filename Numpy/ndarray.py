import numpy as np

arr=np.array(range(1,5))
square=np.array([[4*j+i+1 for i in range(4)] for j in range(4)])
cube=np.array([[[4**2*k+4*j+i+1 for i in range(4)] for j in range(4)] for k in range(4)])

print(arr)
print(square)
print(cube)
print() # 띄우기
print(np.shape(arr))
print(np.shape(square))
print(np.shape(cube))

# print로 출력시 자동으로 개행되서 출력된다.

floatarr=np.array(range(1,10),dtype=float)

class Num:
    def __init__(self,x):
        self.x=x

    def __str__(self):
        return self.x

Numarr=np.array(range(1,10),dtype=Num)
print(Numarr)
# 객체도 오류는 안나는데 제대로 실행되는 것 같지는 않다..

boolarr=np.array(range(1,10),dtype=bool)
print(boolarr)
# bool도 잘 작동한다!

mixedarr1=np.array(["1","2","3"],dtype=int)
print(mixedarr1)

try:mixedarr2=np.array(["1","2","삼"],dtype=int)
except:print("에러발생")

# "삼"은 int로 변경 불가능하니 에러가 발생한다.

mixedarr3=np.array([1,"2","삼"])
print(mixedarr3)

# array안에 다양한 데이터 타입이 존재하는 경우
# 문자열 > 실수형 > 정수형 > 불리언
# 위 순서로 변경된다. 

# ex 정수와 실수가 같이 존재 -> 정수형을 실수형으로 변경

# 리스트와는 다르게 array에서는 데이터 타입이 단일이어야 한다.

arr=np.array(range(1,5))
square=np.array([[4*j+i+1 for i in range(4)] for j in range(4)])
cube=np.array([[[4**2*k+4*j+i+1 for i in range(4)] for j in range(4)] for k in range(4)])


print(square)
print() # 띄우기

# 인덱싱
# [x, y, z ... ] 차원 만큰 해주면 될 듯

print(square[0,3]) # array의 0번 인덱스 [1,2,3,4] 의 3번 인덱스 (4)

# 아래 두 개는 똑같은 역할 수행
# 파이썬 리스트에서의 : 의 역할과 비슷한 느낌
print(square[0]) 
print(square[0,:])

# fancy indexing
# 원하는 값들만 빼오기, [[idx1,idx2,idx3... ]] 이런식으로 써주어야 함.

print(arr)

print(arr[[0,2,3]]) # 원하는 위치의 값들만 빼오기,

# boolean indexing
# r언어 공부했을 때 봤던 거

print(arr)
print(arr>2) # 조건을 만족하는 것은 True 아닌 것은 False인 배열

print(arr[arr>2]) # Fancy indexing 과의 응용, 조건을 만족하는 값만을 추출
