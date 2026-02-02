import pandas as pd


N_VALUES = 1000  # 난수의 갯수
SEED_MIN, SEED_MAX = 1, 100  # 시드 최소값~최대값
K_MIN, K_MAX = 1, 50  # 자기상관 각격 쳐@정하기


# 가로열: 시드값
# 세로열: 자기상관 간격

dic = {str(i): [] for i in range(1, 101)}

# 아래 For문에서
# i는 가로열 시드값
# k는 인덱스+1 (사실상 자기상관간격 상수라고 보면됨. 인덱스는 0에서부터 시작함.)
for i in range(1, 101):
	dic[str(i)] = [k for k in range(1,101)]
# print(dic)
# 데이터프레임생성 (인덱스 추가)
df = pd.DataFrame(dic)

df.to_excel("Output/Test1.xlsx")
print(df)