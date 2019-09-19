'''
Fizz Buzz is a classic programming problem. Here is its slightly modified version.

Write a program that takes the input of two integers: the beginning and the end of the interval (both numbers belong to the interval).

The program should output the numbers from this interval, but if the number is divisible by 3, you should output Fizz instead of it, 
if the number is divisible by 5 - output Buzz, and if it is divisible both by 3 and by 5 - output FizzBuzz.

Output each number or the word on a separate line.
'''

a, b = map(int, input().split())
for i in range(a, b + 1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 ==0:
        print('Buzz')
    else:
        print(i)
