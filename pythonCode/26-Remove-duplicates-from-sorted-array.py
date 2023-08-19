nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


def removeDuplicates(nums) -> int:
    insertIndex = 1
    size = len(nums)
    for i in range(1, size):
        if nums[i - 1] != nums[i]:
            nums[insertIndex] = nums[i]
            insertIndex = insertIndex + 1
    return insertIndex


print(removeDuplicates(nums))
