def merge_sorted_lists(l1: list[int], l2: list[int]) -> list[int]:
    """
    Merges two sorted lists into a single sorted list using Two Pointers.
    
    Time Complexity: O(n + m) where n and m are lengths of l1 and l2.
    Space Complexity: O(n + m) for the resulting list.
    """
    merged = []
    i, j = 0, 0
    
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1
            
    # Append any remaining elements
    merged.extend(l1[i:])
    merged.extend(l2[j:])
    
    return merged

# --- Test Cases ---
if __name__ == "__main__":
    print(f"Merge [1, 3, 5] and [2, 4, 6]: {merge_sorted_lists([1, 3, 5], [2, 4, 6])}")
