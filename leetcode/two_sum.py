from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    look_up = {}
    for index, value in enumerate(nums):
        if target - value in look_up:
            return [look_up[target - value], index]
        else:
            look_up[value] = index
    return [-1, -1]


if __name__ == "__main__":
    nums = [2, 7, 9, 13]
    target = 9
    print(two_sum(nums, target))
