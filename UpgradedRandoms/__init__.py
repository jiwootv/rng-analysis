from .lcg import *
from .middle_square import *
from .XorShift32 import *
from .meresene_twister import *
from .randu import *
if __name__ == "__main__":
	L = LCG.LCG()
	for _ in range(20): print(L.next_float())