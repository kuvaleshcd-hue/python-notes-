from collections import Counter

def count_frequency(elements: list) -> dict:
    """
    Counts the frequency of elements in a list using a Hash Map (Counter).
    
    Time Complexity: O(n)
    Space Complexity: O(k) where k is the number of unique elements.
    """
    # Python's built-in collections.Counter does exactly this efficiently
    return dict(Counter(elements))

def count_frequency_manual(elements: list) -> dict:
    """Manual approach without collections.Counter"""
    freq_map = {}
    for el in elements:
        freq_map[el] = freq_map.get(el, 0) + 1
    return freq_map

# --- Test Cases ---
if __name__ == "__main__":
    lst = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(f"Frequency: {count_frequency(lst)}")
