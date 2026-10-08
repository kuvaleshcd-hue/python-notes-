def find_duplicates(nums: list[int]) -> list[int]:
    """
    Finds duplicate elements in a list using a hash set.
    
    Time Complexity: O(n)
    Space Complexity: O(n) for the sets.
    """
    seen = set()
    duplicates = set()
    
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
            
    return list(duplicates)

# --- Test Cases ---
if __name__ == "__main__":
    print(f"Duplicates in [1, 2, 3, 2, 4, 5, 5]: {find_duplicates([1, 2, 3, 2, 4, 5, 5])}")
    print(f"Duplicates in [1, 2, 3]: {find_duplicates([1, 2, 3])}")
