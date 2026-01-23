# 중앙제곱법
# 분산 개@쓰레기;;
class Middle_Square:
	def __init__(self, seed=1234, digits=4):
		self.x = seed
		self.d = digits
		self.mod = 10**digits

	def next_int(self):
		sq = self.x * self.x
		# 가운데 digits만 뽑기
		# 예: digits=4면 sq를 8자리로 보고 가운데 4자리
		s = str(sq).zfill(self.d * 2)
		mid = s[self.d//2 : self.d//2 + self.d]
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
			if type == "int": self.l.append(self.next_int())
			elif type == "float": self.l.append(self.next_float())
			else: raise ValueError(f"잘못된 Type값입니다. int 또는 float을 입력하십시오. 현재 {type}이/가 입력되었습니다.")
		print(self.l)