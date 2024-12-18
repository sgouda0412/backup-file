class Solution:
    ##Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr):
        ##Your code here
        # max_sum_ = float("-inf")
        # for i in range(len(arr)):
        #     sum_ = 0
        #     for j in range(i, len(arr)):
        #         sum_ += arr[j]
        #         max_sum_ = max(max_sum_, sum_)
        # return max_sum_

        local_max = 0
        global_max = float("-inf")

        for n in arr:
            local_max = max(local_max + n, n)
            if local_max > global_max:
                global_max = local_max
        return global_max


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 3, -8, 7, -1, 2, 3]
    print(sol.maxSubArraySum(arr))
