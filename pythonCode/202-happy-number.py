def happy(n: int) -> bool:
    seen_before_set = set()

    while n not in seen_before_set:
        seen_before_set.add(n)
        n = sumOfSquares(n)

        if n == 1:
            return True
    
    return False

def sumOfSquares(n: int) -> int:
    output = 0
    while n:
        digit = n % 10
        digit = digit ** 2
        output += digit
        n = n // 10
    return output

    # 1 % 10 = 1
    # 1 // 10 = 0, and the while loops exists.
    # since no single digit number squared gives 3 digits this
    # mod 10 trick works to get the single digit. 