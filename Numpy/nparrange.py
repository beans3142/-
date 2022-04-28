import numpy as np

# 아래 두 코드는 같은 역할을 수행함.
# 그냥 파이썬의 range와 비슷한 느낌

arr=np.arange(1,11,1)
print(arr)
arr=np.arange(start=1,stop=11,step=1)
print(arr)

# sorting

# 1차원 정렬의 경우
# 그냥 하면 된다.

arr=np.array([1,4,2,5,7,9,8,-2])
print(arr)
sarr=np.sort(arr)
print(sarr)
arr.sort() # 해당 경우 arr자체를 정렬함.
print(arr)

# 2차원 정렬의 경우
# Axis가 필요하다.

matrix=np.array([i for i in range(15,0,-1)]).reshape(3,5)
print("정렬 전")
print(matrix)
print("axis=0 (같은 행 내 정렬) 정렬 후")
print(np.sort(matrix,axis=0))
print("axis=1 (같은 열 내 정렬) 정렬 후")
print(np.sort(matrix,axis=1))

# argsort (인덱스 반환)

matrix=np.array([i for i in range(15,0,-1)]).reshape(3,5)
print("정렬 전")
print(matrix)
print("axis=0 (같은 행 내 정렬) 정렬 후")
print(np.argsort(matrix,axis=0))
print("axis=1 (같은 열 내 정렬) 정렬 후")
print(np.argsort(matrix,axis=1))

