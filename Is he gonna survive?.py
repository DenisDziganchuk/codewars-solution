# https://www.codewars.com/kata/59ca8246d751df55cc00014c/train/python
def hero(bullets, dragons):
    dragons = dragons * 2
    if bullets >= dragons:
        return True
    else:
        return False
