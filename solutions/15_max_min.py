def find_max_min(nums: list[int]) -> tuple[int, int]:
    """
    Finds the maximum and minimum elements in a list without using built-in functions.
    
    Time Complexity: O(n) - Single pass (Linear Scan).
    Space Complexity: O(1)
    """
    if not nums:
        raise ValueError("List is empty")
        
    max_val = nums[0]
    min_val = nums[0]
    
    for num in nums[1:]:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num
            
    return max_val, min_val

# --- Test Cases ---
if __name__ == "__main__":
    arr = [3, 1, 9, 7, 5, 2, 8]
    mx, mn = find_max_min(arr)
    print(f"Array: {arr}")
    print(f"Max: {mx}, Min: {mn}")
