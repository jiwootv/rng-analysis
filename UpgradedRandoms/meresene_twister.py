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
