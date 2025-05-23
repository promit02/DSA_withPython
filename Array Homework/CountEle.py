from collections import Counter

def count_frequency(arr):
    return dict(Counter(arr))

print(count_frequency([1, 2, 2, 3]))  # Output: {1: 1, 2: 2, 3: 1}
