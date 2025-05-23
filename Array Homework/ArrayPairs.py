def find_pairs_with_sum(arr, target):
    pairs = []
    seen = set()
    for num in arr:
        if (target - num) in seen:
            pairs.append((target - num, num))
        seen.add(num)
    return pairs

print(find_pairs_with_sum([1, 2, 3, 4], 5))  # Output: [(1, 4), (2, 3)]
