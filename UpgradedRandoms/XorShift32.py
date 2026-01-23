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

	def get_value_list(self, len: int, type: str):
		"""
		len: 값의 길이
		Type: 타입. u32 또는 float을 선택 가능합니다.
		"""
		self.l = []
		for i in range(len):
			if type == "int": self.l.append(self.next_int())
			elif type == "float": self.l.append(self.next_float())
			else: raise ValueError(f"잘못된 Type값입니다. u32 또는 float을 입력하십시오. 현재 {type}이/가 입력되었습니다.")
		print(self.l)