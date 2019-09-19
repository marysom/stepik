'''MKAD

The length of the Moscow Ring Road (MKAD) is 109 kilometers. Biker Vasya starts from the zero kilometer 
of MKAD and drives with a speed of V kilometers per hour. On which mark will he stop after T hours?

Input data format
The program gets integers V and T as input. If V > 0, then Vasya moves in a positive direction along MKAD, 
if the value of V < 0 – in the negative direction. 0 ≤ T ≤ 1000, -1000 ≤ V ≤ 1000.

Output data format
The program should output an integer from 0 to 108 - the mark on which Vasya stops.
'''

V = int(input())
T = int(input())
print(T*V % 109)
