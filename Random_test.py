import UpgradedRandoms

L = UpgradedRandoms.LCG()
M = UpgradedRandoms.Middle_Square()
X = UpgradedRandoms.Xorshift32()
R = UpgradedRandoms.Meresene_twister()

M.get_value_list(61, "float")