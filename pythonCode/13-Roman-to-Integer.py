def romantToInt(s: str) -> int:
    translation = {"I": 1, "V": 5, "X": 10,
                   "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    previousVal = 10000
    for char in s:
        if translation[char] > previousVal:
            result -= 2 * previousVal
            result += translation[char]
            previousVal = translation[char]
        else:
            result += translation[char]
            previousVal = translation[char]
    print(result)
    return result


input = "MCMXCIV"
romantToInt(input)
