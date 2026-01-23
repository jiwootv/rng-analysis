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