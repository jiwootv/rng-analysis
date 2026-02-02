# 메르센 트위스트
# python 기본 random 라이브러리가 이 알고리즘을 사용해서 넣어봄
# 딸깍 ㅋㅋㅋㅋㅋ
import random

class Meresene_twister:
	def __init__(self, seed=None):
		self.rng = random.Random(seed)

	def next_float(self):
		return self.rng.random()   # [0, 1)

	def next_int(self, a=0, b=2**32-1):
		return self.rng.randint(a, b)

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
		return self.l