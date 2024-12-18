class Solution:
    def maxProduct(self, arr):
        # max_product = float("-inf")
        # for i in range(len(arr)):
        #     prod = 1
        #     for j in range(i, len(arr)):
        #         prod *= arr[j]
        #         max_product = max(prod, max_product)
        # return max_product

        max_product = current_max = current_min = arr[0]
        for num in arr[1:]:
            if num < 0:
                current_max, current_min = current_min, current_max

            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)

            max_product = max(max_product, current_max)

        return max_product


if __name__ == "__main__":
    sol = Solution()
    arr = [-2, 6, -3, -10, 0, 2]
    print(sol.maxProduct(arr))
