class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle(head: ListNode) -> ListNode:
    """
    Finds the middle node of a linked list.
    If there are two middle nodes, returns the second one.
    
    Approach: Fast and Slow Pointers
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    slow = head
    fast = head
    
    # Fast moves twice as fast. When fast reaches the end, slow is in the middle.
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow

# --- Test Cases ---
if __name__ == "__main__":
    # 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    mid = find_middle(head)
    print(f"Middle of 1->2->3->4->5 is: {mid.val}")
    
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6
    head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    mid2 = find_middle(head2)
    print(f"Middle of 1->2->3->4->5->6 is: {mid2.val}")
