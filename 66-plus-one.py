from typing import List


input1 = [4, 1, 2, 3]
input2 = [9, 9, 9]


def plus_one(digits: List[int]) -> List[int]:
    arrLength = len(digits)
    i = arrLength - 1
    while i >= 0:
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
        i -= 1
    return [1] + digits


a = plus_one(input1)
b = plus_one(input2)

print(a)
print(b)

