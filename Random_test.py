import UpgradedRandoms

L = UpgradedRandoms.LCG()
M = UpgradedRandoms.Middle_Square()
X = UpgradedRandoms.Xorshift32()
R = UpgradedRandoms.Meresene_twister()
for i in range(100): print(L.next_float())
print("____")
for i in range(100): print(M.next_float())
print("____")
for i in range(100): print(X.next_float())
print("____")
for i in range(100): print(R.next_float())
print("____")