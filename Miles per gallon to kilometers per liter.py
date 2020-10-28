# https://www.codewars.com/kata/557b5e0bddf29d861400005d/train/python
def converter(mpg):
    gallon = 4.54609188
    miles = 1.609344
    return round(mpg * miles / gallon, 2)
