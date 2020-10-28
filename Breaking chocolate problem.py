# https://www.codewars.com/kata/534ea96ebb17181947000ada/train/python
def breakChocolate(n, m):
    if m == 0 or n == 0:
        return 0
    else:
        return n * m - 1
