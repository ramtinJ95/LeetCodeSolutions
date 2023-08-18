nums = [1, 1, 2, 3, 4, 4, 5, 6, 6]


def removeduplicates(nums: List[int]) -> int:
    for i in range(len(nums) - 1):
        if i == 0:
            continue
        if nums[i - 1] != nums[i]:
