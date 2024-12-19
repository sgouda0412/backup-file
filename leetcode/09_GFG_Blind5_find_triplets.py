class Solution:
    def findTriplets(self, arr, k):
        arr.sort()
        triplets = []

        for i in range(len(arr) - 2):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            left = i + 1
            right = len(arr) - 1

            while left < right:
                sum = arr[i] + arr[left] + arr[right]
                if sum == k:
                    triplets.append([arr[i], arr[left], arr[right]])
                    while left < right and arr[left] == arr[left + 1]:
                        left += 1
                    while left < right and arr[right] == arr[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum < k:
                    left += 1
                else:
                    right -= 1
        return triplets


if __name__ == "__main__":
    sol = Solution()
    arr = [0, -1, 2, -3, 1]
    k = -2
    print(sol.findTriplets(arr, k))
