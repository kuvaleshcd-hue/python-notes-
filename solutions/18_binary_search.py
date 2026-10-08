def binary_search(arr: list[int], target: int) -> int:
    """
    Performs Binary Search on a sorted array to find the target.
    Returns the index if found, else -1.
    
    Time Complexity: O(log n) - halves the search space each iteration.
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1 # Target is in the right half
        else:
            right = mid - 1 # Target is in the left half
            
    return -1

# --- Test Cases ---
if __name__ == "__main__":
    sorted_arr = [1, 3, 5, 7, 9, 11, 15]
    print(f"Array: {sorted_arr}")
    print(f"Index of 7: {binary_search(sorted_arr, 7)}")
    print(f"Index of 10: {binary_search(sorted_arr, 10)}")
