from collections import Counter

def is_anagram(s1: str, s2: str) -> bool:
    """
    Checks if two strings are anagrams of each other.
    
    Time Complexity: O(n)
    Space Complexity: O(1) - hash map stores at most 26 unique characters.
    """
    # Clean the strings: remove spaces and lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    if len(s1) != len(s2):
        return False
        
    return Counter(s1) == Counter(s2)

# --- Test Cases ---
if __name__ == "__main__":
    print(f"Anagrams ('listen', 'silent'): {is_anagram('listen', 'silent')}")
    print(f"Anagrams ('hello', 'world'): {is_anagram('hello', 'world')}")
