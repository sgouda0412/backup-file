class Solution:
    def search_in_sorted_and_rotated_arr(self, arr, key):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == key:
                return mid
            # check for sorted left part
            if arr[left] <= arr[mid]:
                if arr[left] <= key < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # check for right sorted part
                if arr[mid] < key <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    key = 3
    print(sol.search_in_sorted_and_rotated_arr(arr, key))
