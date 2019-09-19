'''
Write the function filter_positive, which takes a list of numbers as input, and, not changing this list, 
returns the new list containing only the positive elements of it

You should not write input and output, only a function.
'''

def filter_positive(ls):
    out = list()
    for i in ls:
        if i > 0:
            out.append(i)
    return out
