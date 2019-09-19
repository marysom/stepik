'''
Write a program, which takes the list of numbers and creates a new list, which contains all the elements of this list, 
excluding duplicates.

Write your solutions as a function f(ls).
'''

def f(ls):
    out = ls
    for i in ls:
        if ls.count(i) > 1:
            out.remove(i)
    return out
