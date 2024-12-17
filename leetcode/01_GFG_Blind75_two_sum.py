class Solution:
    def twoSum(self, arr, target):
        # arr.sort()
        # left = 0
        # right = len(arr) - 1

        # while left < right:
        #     if arr[left] + arr[right] < target:
        #         left += 1
        #     elif arr[left] + arr[right] > target:
        #         right -= 1
        #     else:
        #         return [arr[left], arr[right]]
        # return []

        # s = set()
        # for i in range(len(arr)):
        #     if target - arr[i] in s:
        #         return [target - arr[i], arr[i]]
        #     else:
        #         s.add(arr[i])
        # return []

        seen = {}
        for idx, val in enumerate(arr):
            diff = target - val
            if diff in seen:
                return [diff, val]
            seen[val] = idx
        return []


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 9, 10, 4, 15]
    target = 12
    print(sol.twoSum(arr, target))
