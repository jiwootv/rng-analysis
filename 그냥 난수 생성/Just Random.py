# 그냥 난수 뽑아주는 내용
import random
import matplotlib.pyplot as plt


k = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(100):
	a = random.randint(0, 9)
	k[a] += 1

plt.bar([i for i in range(1,11)],k)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Random guys")
plt.show()