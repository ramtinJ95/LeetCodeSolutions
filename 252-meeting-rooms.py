from typing import List


input1 = [[0, 30], [5, 10], [15, 20]]
input2 = [[7, 10], [2, 4]]


def meetingrooms(input: List[List[int]]) -> bool:
    input.sort()
    for i, interval in enumerate(input):
        print(input)
        if(i+1 >= len(input)):
            return True
        i1 = input[i]
        i2 = input[i+1]
        if i1[1] > i2[0]:
            return False
    return True


print(meetingrooms(input1))
print(meetingrooms(input2))
