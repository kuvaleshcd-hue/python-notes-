def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome (reads the same forwards and backwards).
    Ignores spaces, punctuation, and capitalization.
    
    Approach:
    Use two pointers (left and right). Move them towards the center, skipping
    non-alphanumeric characters. Compare the characters at the pointers.
    
    Time Complexity: O(n) - We traverse the string at most once.
    Space Complexity: O(1) - We only use two integer pointers.
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters from the left
        if not s[left].isalnum():
            left += 1
            continue
        
        # Skip non-alphanumeric characters from the right
        if not s[right].isalnum():
            right -= 1
            continue
            
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
        
    return True

# --- Test Cases ---
if __name__ == "__main__":
    print(f"is_palindrome('racecar') -> {is_palindrome('racecar')}")
    print(f"is_palindrome('A man, a plan, a canal: Panama') -> {is_palindrome('A man, a plan, a canal: Panama')}")
    print(f"is_palindrome('hello') -> {is_palindrome('hello')}")
