def remove_duplicates_preserve_order(nums: list) -> list:
    """
    Removes duplicates from a list while keeping the original order.
    
    Time Complexity: O(n)
    Space Complexity: O(n) - Using a set to track seen elements.
    """
    seen = set()
    result = []
    
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
            
    return result

# --- Test Cases ---
if __name__ == "__main__":
    arr = [3, 1, 2, 3, 1, 4, 2]
    print(f"Original: {arr}")
    print(f"Unique (ordered): {remove_duplicates_preserve_order(arr)}")
