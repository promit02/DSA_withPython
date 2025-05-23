def longest_consecutive_sequence(arr):
    nums = set(arr)
    longest = 0
    for num in nums:
        if num - 1 not in nums:
            length = 1
            while num + length in nums:
                length += 1
            longest = max(longest, length)
    return longest

print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))  # Output: 4
