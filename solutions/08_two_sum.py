def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Finds the indices of two numbers that add up to a target sum.
    Uses a hash map for O(1) lookups.
    
    Time Complexity: O(n)
    Space Complexity: O(n) for the hash map.
    """
    # Maps number -> its index
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
        
    return []

# --- Test Cases ---
if __name__ == "__main__":
    print(f"Two sum for [2, 7, 11, 15], target=9: {two_sum([2, 7, 11, 15], 9)}")
    print(f"Two sum for [3, 2, 4], target=6: {two_sum([3, 2, 4], 6)}")
