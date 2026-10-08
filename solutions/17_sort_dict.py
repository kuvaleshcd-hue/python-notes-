def sort_dict_by_value(d: dict, reverse: bool = False) -> dict:
    """
    Sorts a dictionary based on its values instead of keys.
    
    Time Complexity: O(n log n) - because of the sorting algorithm.
    Space Complexity: O(n) - to store the new sorted dictionary.
    """
    # dict.items() gives (key, value) pairs
    # key=lambda x: x[1] tells the sort function to sort based on the second item (the value)
    sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=reverse)
    
    return dict(sorted_items)

# --- Test Cases ---
if __name__ == "__main__":
    my_dict = {'apple': 10, 'banana': 5, 'cherry': 20}
    print(f"Original: {my_dict}")
    print(f"Sorted by value (Ascending): {sort_dict_by_value(my_dict)}")
    print(f"Sorted by value (Descending): {sort_dict_by_value(my_dict, reverse=True)}")
