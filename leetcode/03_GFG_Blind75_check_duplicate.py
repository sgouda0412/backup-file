class Solution:

    def checkDuplicates(self, arr):
        # code here
        seen = set()
        for i in arr:
            if i in seen:
                return True
            seen.add(i)
        return False


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 1]
    print(sol.checkDuplicates(arr))
