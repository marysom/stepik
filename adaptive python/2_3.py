'''Snail
Snail creeps up the vertical pole of height H feets. Per day it goes A feets up, and per night it goes B feets down. 
In which day the snail will reach the top of the pole?

Input data format
On the input the program receives non-negative integers H, A, B, where H > B and A > B. Every integer does not exceed 100.
'''

from math import *
H = int(input())
A = int(input())
B = int(input())
print(ceil((H-B)/(A-B)))
