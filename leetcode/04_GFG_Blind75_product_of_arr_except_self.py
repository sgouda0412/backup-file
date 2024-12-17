class Solution:
    def productExceptSelf(self, arr):
        # code here
        # x = []
        # for i in range(len(arr)):
        #     prod = 1
        #     for j in range(len(arr)):
        #         if i != j:
        #             prod = prod * arr[j]
        #     x.append(prod)
        # return x
        # code here
        n = len(arr)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * arr[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * arr[i + 1]

        result = [prefix[i] * suffix[i] for i in range(n)]

        return result


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    print(sol.productExceptSelf(arr))
