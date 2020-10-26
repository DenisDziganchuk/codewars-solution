# https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python
def get_grade(s1, s2, s3):
    d = (s1 + s2 + s3) / 3.0
    if 90 <= d <= 100:
        return 'A'
    elif 80 <= d < 90:
        return 'B'
    elif 70 <= d < 80:
        return 'C'
    elif 60 <= d < 70:
        return 'D'
    else:
      return "F"
