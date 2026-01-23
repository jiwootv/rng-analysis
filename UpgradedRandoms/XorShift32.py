class Xorshift32:
	def __init__(self, seed=2463534242):
		self.x = seed & 0xFFFFFFFF

	def next_u32(self):
		x = self.x
		x ^= (x << 13) & 0xFFFFFFFF
		x ^= (x >> 17) & 0xFFFFFFFF
		x ^= (x << 5)  & 0xFFFFFFFF
		self.x = x & 0xFFFFFFFF
		return self.x

	def next_float(self):
		return self.next_u32() / 2**32