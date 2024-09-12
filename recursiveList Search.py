def recursive_search(lst, target, index=0):
    if index >= len(lst):
        return -1  # Target not found
    if lst[index] == target:
        return index
    return recursive_search(lst, target, index + 1)

# Example usage
elements = [5, 3, 7, 1, 9]
print("Index of 7:", recursive_search(elements, 7))
print("Index of 10:", recursive_search(elements, 10))
