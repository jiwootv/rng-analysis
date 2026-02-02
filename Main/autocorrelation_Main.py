import BaseCode
import RngModels
import pandas as pd

N_VALUES = 10000  # 난수의 갯수
SEED_MIN, SEED_MAX = 1, 100  # 시드 최소값~최대값
K_MIN, K_MAX = 1, 50  # 자기상관 각격 쳐@정하기

# 가로열: 시드값
# 세로열: 자기상관 간격
sumang = 0

dic = {str(i): [] for i in range(1, 101)}

# 아래 For문에서
# i는 가로열 시드값
# k는 인덱스+1 (사실상 자기상관간격 상수라고 보면됨. 인덱스는 0에서부터 시작함.)
for i in range(SEED_MIN, SEED_MAX+1):
    L = RngModels.LCG(i)
    llist = L.get_value_list(N_VALUES+1, "u32")
    for k in range(K_MIN, K_MAX + 1):
        a = BaseCode.autocorr(llist, k)
        dic[str(i)].append(a)
        sumang += a
# print(dic)
# 데이터프레임생성 (인덱스 추가)
df = pd.DataFrame(dic)


df.to_excel("Output/LCG_Testdata1.xlsx")
print(sumang/((SEED_MAX-SEED_MIN+1)*(K_MAX-K_MIN+1)))