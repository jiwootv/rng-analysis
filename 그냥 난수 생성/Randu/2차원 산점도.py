import matplotlib.pyplot as plt
import UpgradedRandoms

isol_gay = 10000
alpha = 1
point_size = 1
color1, color2 = "blue", 'red'
name = "Randu"

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
plot_2d_scatter(UpgradedRandoms.Randu.get_value_list(999, 10000), color="red")
# plot_3d_scatter(chuck_chu)