import random
import matplotlib.pyplot as plt

pos = [_-_ for _ in range(1, 696969)]
# [0, 0, ..., 0]
# [(0, 0), (0,0)

def hehehehehe(l):
	for i in range(l):
		random.seed(i)
		pos[i]  = (i, random.randint(1, l+1))
	plt.scatter([pos[k][0] for k in range(1, l)], [pos[k][1] for k in range(1, l)])
	plt.show()

hehehehehe(69)
