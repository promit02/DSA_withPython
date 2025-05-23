def majority_element(arr):
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
        if count[num] > len(arr) // 2:
            return num
    return None

print(majority_element([3, 3, 4, 3, 5]))  # Output: 3
