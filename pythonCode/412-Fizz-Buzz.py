def fizzBuzz(n: int):
    output = []
    fizz_hash = {3: 'Fizz', 5: 'Buzz'}
    divisors = [3, 5]
    for i in range(1, n+1):
        ans_string = []
        for divisor in divisors:
            if i % divisor == 0:
                ans_string.append(fizz_hash[divisor])
        if not ans_string:
            ans_string.append(str(i))
        output.append(''.join(ans_string))
    return output


input = 3
print(fizzBuzz(input))
input = 5
print(fizzBuzz(input))
input = 15
print(fizzBuzz(input))
