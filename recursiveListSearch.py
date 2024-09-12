def recursive_search(lst, target, index=0):
    if index >= len(lst):
        return -1  # Target not found
    if lst[index] == target:
        return index
    return recursive_search(lst, target, index + 1)

def main():
    # Input list elements
    elements = []
    print("Enter list elements (type 'done' to finish):")
    while True:
        item = input("Add item: ")
        if item.lower() == 'done':
            break
        elements.append(item)
    
    # Input search target
    target = input("Enter item to search for: ")
    
    # Perform search
    index = recursive_search(elements, target)
    
    if index != -1:
        print(f"Item '{target}' found at index {index}.")
    else:
        print(f"Item '{target}' not found in the list.")

if __name__ == "__main__":
    main()

