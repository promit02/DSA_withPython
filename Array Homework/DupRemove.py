def remove_duplicates(arr):
    return list(dict.fromkeys(arr))

print(remove_duplicates([1, 2, 2, 3, 3]))  # Output: [1, 2, 3]
