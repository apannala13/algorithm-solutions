from typing import List

"""
Binary search implementation on a sorted array to find target integer,
O(log n) time complexity
"""


def binary_search(nums:List[int], target:int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r)//2
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid
    return 0


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(binary_search(nums, target))
