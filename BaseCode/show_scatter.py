"""
2026.02.02 오전 2:02 마지막 수정됨.
파일명: show_catter
설명: 리스트 입력받고 산점도를 보여주는 함수들의 모음.
3차원, 2차원 산점도를 보여줄 수 있다.
"""

import matplotlib.pyplot as plt


class ShowScatter:
	def __init__(self, nums, title, n=None, point_size=5, color="blue", alpha=0.7):
		self.nums = nums
		self.title = title
		self.n = n
		self.point_size = point_size
		self.color = color
		self.alpha = alpha

	def plot_2d_scatter(self):
		if self.n is None or self.n > len(self.nums) - 1:
			self.an = len(self.nums) - 1

		x = self.nums[:self.an]
		y = self.nums[1:self.an + 1]

		plt.figure()
		plt.scatter(x, y, s=self.point_size, alpha=self.alpha, color=self.color)
		plt.xlabel("x_i")
		plt.ylabel("x_{i+1}")
		plt.title(self.title)
		plt.show()

	def plot_3d_scatter(self):
		# n: 점 개수 (x_i, x_{i+1}, x_{i+2})라서 최소 3개 필요
		self.max_n = len(self.nums) - 2
		if self.max_n <= 0:
			raise ValueError("nums 길이가 너무 짧음 (최소 3개 필요)")
		if self.n is None or self.n > self.max_n:
			self.an = self.max_n

		x = self.nums[:self.an]
		y = self.nums[1:self.an + 1]
		z = self.nums[2:self.an + 2]

		fig = plt.figure()
		ax = fig.add_subplot(111, projection="3d")
		ax.scatter(x, y, z, s=self.point_size, alpha=self.alpha, color=self.color)

		ax.set_xlabel("x_i")
		ax.set_ylabel("x_{i+1}")
		ax.set_zlabel("x_{i+2}")
		ax.set_title(self.title)

		plt.show()

if __name__ == "__main__":
	import RngModels
	R = RngModels.Randu()
	k = R.get_value_list(1, 10000)
	L = RngModels.LCG()
	l = L.get_value_list(10000, "u32")
	M = RngModels.Middle_Square()
	a = M.get_value_list(1000, 'int')
	S = ShowScatter(a, "Midsquare show", point_size=5)
	S.plot_3d_scatter()