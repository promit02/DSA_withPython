def find_second_largest(arr):
    unique = list(set(arr))
    unique.sort()
    return unique[-2] if len(unique) >= 2 else None

print(find_second_largest([3, 8, 6, 5]))  # Output: 6
