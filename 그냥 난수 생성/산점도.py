import random
import matplotlib.pyplot as plt

pos = [_-_ for _ in range(1, 696969)]
# [0, 0, ..., 0]
# [(0, 0), (0,0)

def angang(sibal):
	for i in range(sibal):
		random.seed(i)
		pos[i]  = (i, random.randint(1, sibal+1))
	plt.scatter([pos[k][0] for k in range(1, sibal)], [pos[k][1] for k in range(1, sibal)])
	plt.show()

angang(69)