#Task 1
# --------------------------------------------
# Step 1: Define the Binary Search function
# --------------------------------------------
def binary_search(arr, target):
    """Perform binary search on a sorted list 'arr' to find the target value.
    Returns the index of the target if found, otherwise returns -1."""
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2 

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# --------------------------------------------
# Step 2: Let’s test it with an example
# --------------------------------------------
if __name__ == "__main__":
    numbers = [2, 4, 7, 10, 13, 18, 21, 25, 30]
    print("Sorted List:", numbers)
    target_value = int(input("Enter a number to search: "))
    result = binary_search(numbers, target_value)
    # --------------------------------------------
    # Step 3: Print results
    # --------------------------------------------
    if result != -1:
        print(f"Found {target_value} at index {result}")
    else:
        print(f"{target_value} not found in the list")