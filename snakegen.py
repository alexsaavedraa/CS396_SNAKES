from snakegeneration import RANDOM_GEN
import os
import sys

id = sys.argv[1] 

rG = RANDOM_GEN(id)
rG.Generate_And_Run()
