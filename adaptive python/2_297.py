'''
There are two horses on a chess board and four coordintes x_1x1 , y_1y1 , x_2x2 , y_2y2  are typed in. 
Determine, whether they can hit each other or not. 

INPUT
Four integer coordinates in the following sequence: x_1, y_1, x_2, y_2x1 ,y1 ,x2 ,y2 . The coordinates are not the same.

OUTPUT
"YES" (uppercase), if they hit each other and "NO" if they don't.
'''

x1, y1, x2, y2 = map(int, input().split())
if (abs(x1-x2) == 2 and abs(y1-y2) == 1) or (abs(x1-x2) == 1 and abs(y1-y2) == 2):
    print('YES')
else: print('NO')
