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

	def get_value_list(self, len: int, type: str):
		"""
		len: 값의 길이
		Type: 타입. u32 또는 float을 선택 가능합니다.
		"""
		self.l = []
		for i in range(len):
			if type == "u32": self.l.append(self.next_u32())
			elif type == "float": self.l.append(self.next_float())
			else: raise ValueError(f"잘못된 Type값입니다. u32 또는 float을 입력하십시오. 현재 {type}이/가 입력되었습니다.")
		print(self.l)
		return self.l