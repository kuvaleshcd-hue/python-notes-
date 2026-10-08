def reverse_string(s: str) -> str:
    """
    Reverses a string without using Python's built-in slicing (s[::-1]).
    
    Approach:
    Use two pointers, one at the beginning and one at the end of the string.
    Swap the characters at the pointers and move them towards the center.
    Since strings are immutable in Python, we convert it to a list first.
    
    Time Complexity: O(n) - We iterate through half of the string.
    Space Complexity: O(n) - We create a list of characters of size n.
    """
    # Convert string to list of characters because strings are immutable in Python
    chars = list(s)
    left, right = 0, len(chars) - 1
    
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
        
    return "".join(chars)

# --- Test Cases ---
if __name__ == "__main__":
    print(f"reverse_string('hello') -> '{reverse_string('hello')}'")
    print(f"reverse_string('Python') -> '{reverse_string('Python')}'")
    print(f"reverse_string('') -> '{reverse_string('')}'")
