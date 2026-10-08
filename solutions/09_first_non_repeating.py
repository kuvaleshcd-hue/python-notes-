def first_non_repeating(s: str) -> str:
    """
    Finds the first non-repeating character in a string.
    
    Time Complexity: O(n) - Two passes through the string.
    Space Complexity: O(1) - The hash map holds at most 26 characters (if only lowercase English letters).
    """
    char_counts = {}
    
    # First pass: count frequencies
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
        
    # Second pass: find the first one with count == 1
    for char in s:
        if char_counts[char] == 1:
            return char
            
    return "" # Return empty string if all characters repeat

# --- Test Cases ---
if __name__ == "__main__":
    print(f"First non-repeating in 'swiss': '{first_non_repeating('swiss')}'")
    print(f"First non-repeating in 'aabbcc': '{first_non_repeating('aabbcc')}'")
