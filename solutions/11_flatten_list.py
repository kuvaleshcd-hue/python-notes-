def flatten_list(nested_list: list) -> list:
    """
    Flattens a deeply nested list using recursion.
    
    Time Complexity: O(n) where n is the total number of elements.
    Space Complexity: O(d) for the call stack, where d is the maximum depth.
    """
    flat = []
    for element in nested_list:
        if isinstance(element, list):
            # Recursively flatten
            flat.extend(flatten_list(element))
        else:
            flat.append(element)
    return flat

# --- Test Cases ---
if __name__ == "__main__":
    nested = [1, [2, [3, 4], 5], 6]
    print(f"Flatten {nested}: {flatten_list(nested)}")
