import RngModels
import numpy
import math
import BaseCode

L = RngModels.LCG()
M = RngModels.Middle_Square()
X = RngModels.Xorshift32()
R = RngModels.Meresene_twister()

# 예시: 중앙제곱법 표준편차와 값 샘플 뽑기
midsqr = M.get_value_list(1000, "float")
print(math.sqrt(numpy.var(midsqr)))

