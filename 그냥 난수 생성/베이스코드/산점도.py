import matplotlib.pyplot as plt

isol_gay = 10000
alpha = 1
point_size = 1
color1, color2 = "blue", 'red'
name = "Randu"


def randu(seed, n):
	m = 2 ** 31
	a = 65539
	x = seed
	res = []
	for _ in range(n):
		x = (a * x) % m
		res.append(x / m)  # 정규화
	return res


# 중앙제곱법
# 분산 개@쓰레기;;
class Middle_Square:
	def __init__(self, seed=58774485, digits=20):
		self.x = seed
		self.d = digits
		self.mod = 10 ** digits

	def next_int(self):
		sq = self.x * self.x
		# 가운데 digits만 뽑기
		# 예: digits=4면 sq를 8자리로 보고 가운데 4자리
		s = str(sq).zfill(self.d * 2)
		mid = s[self.d // 2: self.d // 2 + self.d]
		self.x = int(mid) % self.mod
		return self.x

	def next_float(self):
		return self.next_int() / self.mod

	def get_value_list(self, len: int, type: str):
		"""
		len: 값의 길이
		Type: 타입. int 또는 float을 선택 가능합니다.
		"""
		self.l = []
		for i in range(len):
			if type == "int":
				self.l.append(self.next_int())
			elif type == "float":
				self.l.append(self.next_float())
			else:
				raise ValueError(f"잘못된 Type값입니다. int 또는 float을 입력하십시오. 현재 {type}이/가 입력되었습니다.")
		# print(self.l)
		return self.l


class LCG:
	def __init__(self, seed=1, a=1664525, c=1013904223, m=2 ** 32):
		self.x = seed
		self.a = a
		self.c = c
		self.m = m

	def next_u32(self):
		self.x = (self.a * self.x + self.c) % self.m
		return self.x

	def next_float(self):
		return self.next_u32() / self.m

	def get_value_list(self, len: int, type: str):
		"""
		len: 값의 길이
		Type: 타입. u32 또는 float을 선택 가능합니다.
		"""
		self.l = []
		for i in range(len):
			if type == "u32":
				self.l.append(self.next_u32())
			elif type == "float":
				self.l.append(self.next_float())
			else:
				raise ValueError(f"잘못된 Type값입니다. u32 또는 float을 입력하십시오. 현재 {type}이/가 입력되었습니다.")

		return self.l


### 리스트 넣기 ###

L = LCG()
chuck_chu = L.get_value_list(isol_gay, "u32")


# M = Middle_Square()
# anggymocchi = M.get_value_list(isol_gay, "float")
# yayaya = randu(1, 10000)

##############

def plot_2d_scatter(nums, color, n=None):
	if n is None or n > len(nums) - 1:
		n = len(nums) - 1

	x = nums[:n]
	y = nums[1:n + 1]

	plt.figure()
	plt.scatter(x, y, s=point_size, alpha=alpha)
	plt.xlabel("x_i")
	plt.ylabel("x_{i+1}")
	plt.title(f"2D Scatter Plot of {name}")
	plt.show()


#######

def plot_3d_scatter(nums, n=None, s=5, alpha=0.4):
	# n: 점 개수 (x_i, x_{i+1}, x_{i+2})라서 최소 3개 필요
	max_n = len(nums) - 2
	if max_n <= 0:
		raise ValueError("nums 길이가 너무 짧음 (최소 3개 필요)")
	if n is None or n > max_n:
		n = max_n

	x = nums[:n]
	y = nums[1:n + 1]
	z = nums[2:n + 2]

	fig = plt.figure()
	ax = fig.add_subplot(111, projection="3d")
	ax.scatter(x, y, z, s=s, alpha=alpha)

	ax.set_xlabel("x_i")
	ax.set_ylabel("x_{i+1}")
	ax.set_zlabel("x_{i+2}")
	ax.set_title(f"3D Scatter Plot of {name}")

	plt.show()


# nums = [0.12, 0.45, 0.78, 0.33, 0.91, 0.04]
# plot_2d_scatter(randu(999, 10000), color="red")
plot_3d_scatter(randu(999, 10000))