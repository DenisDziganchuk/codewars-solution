# https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/train/python
def past(h, m, s):
    h = h * 3600 * 1000
    m = m * 60 * 1000
    s = s * 1000
    return h + m + s
