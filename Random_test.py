import UpgradedRandoms
import numpy
import math

L = UpgradedRandoms.LCG()
M = UpgradedRandoms.Middle_Square()
X = UpgradedRandoms.Xorshift32()
R = UpgradedRandoms.Meresene_twister()

# 예시: 중앙제곱법 표준편차와 값 샘플 뽑기
midsqr = M.get_value_list(1000, "float")
print(math.sqrt(numpy.var(midsqr)))

