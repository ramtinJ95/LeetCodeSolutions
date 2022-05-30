# Most important learning here that i messed up and got time limit exceed for is that we cannot forget to exclude the middle
# that means that i forgot to do the midIndex - 1 and midIndex + 1 parts and thus got stuck in an infinite loop!
def search(self, nums: List[int], target: int) -> int:
    leftPointer = 0
    rightPointer = len(nums)-1
    while leftPointer <= rightPointer:
        midIndex = leftPointer + (rightPointer - leftPointer) // 2
        if nums[midIndex] == target:
            return midIndex
        if target > nums[midIndex]:
            leftPointer = midIndex + 1
        if target < nums[midIndex]:
            rightPointer = midIndex - 1
    return -1