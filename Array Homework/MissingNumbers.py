def find_missing(arr, n):
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(arr)

print(find_missing([1, 2, 4, 5], 5))  # Output: 3
