import numpy as np

def autocorr(x, k):
	x = np.array(x)
	n = len(x)

	xbar = x.mean()

	a = x[:n-k] - xbar
	b = x[k:] - xbar

	num = np.sum(a * b)

	# 정규화용 분모
	# 분산 안나눈거
	den = np.sum((x - xbar)**2)

	# pair = np.vstack([a, b])
	# print(pair)
	return num / den

if __name__ == "__main__":
	import RngModels
	x = RngModels.LCG(seed=7).get_value_list(1000, "float")
	# print(x)
	for k in range(1,6):
		print(k, autocorr(x, k))