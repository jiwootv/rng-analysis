class Randu:
	def __init__(self):
		pass

	def get_value_list(self, seed, n):
		m = 2 ** 31
		a = 65539
		x = seed
		res = []
		for _ in range(n):
			x = (a * x) % m
			res.append(x / m)  # 정규화
		return res