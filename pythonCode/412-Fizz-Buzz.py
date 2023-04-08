def fizzBuzz(n: int):
    output = []
    for i in range(1, n+1):
        if (i % 3 == 0 and i % 5 == 0):
            output.append("FizzBuzz")
        elif (i % 3 == 0):
            output.append("Fizz")
        elif (i % 5 == 0):
            output.append("Buzz")
        else:
            output.append(str(i))

    return output


input = 3
print(fizzBuzz(input))
input = 5
print(fizzBuzz(input))
input = 15
print(fizzBuzz(input))
