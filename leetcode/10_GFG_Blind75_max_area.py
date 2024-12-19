def maxArea(A, le):
    # code here
    l = 0
    r = le - 1
    max_area = 0

    while l < r:
        h = min(A[l], A[r])
        b = r - l
        max_area = max(max_area, h * b)

        if A[l] < A[r]:
            l += 1
        else:
            r -= 1
    return max_area


if __name__ == "__main__":
    arr = [3, 1, 2, 4, 5]
    le = 5
    print(maxArea(arr, le))
