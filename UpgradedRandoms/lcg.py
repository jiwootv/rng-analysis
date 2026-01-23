#

class LCG:
	def __init__(self, seed=1, a=1664525, c=1013904223, m=2**32):
		self.x = seed
		self.a = a
		self.c = c
		self.m = m

	def next_u32(self):
		self.x = (self.a * self.x + self.c) % self.m
		return self.x

	def next_float(self):
		return self.next_u32() / self.m