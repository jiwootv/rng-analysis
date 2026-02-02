import numpy as np

x = np.arange(10)      # 예시: [0,1,2,3,4,5,6,7,8,9]
n = len(x)
k = 3

a = x[:n-k]            # 길이 n-k
b = x[k:]              # 길이 n-k

print(a)               # [0 1 2 3 4 5 6]
print(b)               # [3 4 5 6 7 8 9]

pair = np.vstack([a, b])   # (2, n-k) 모양으로 쌓기
print(pair[0][0], pair[1][0])
print(pair.shape)      # (2, 7)
