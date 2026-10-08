class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head: ListNode) -> bool:
    """
    Detects if a linked list has a cycle using Floyd's Tortoise and Hare algorithm.
    
    Time Complexity: O(n)
    Space Complexity: O(1) - only two pointers used.
    """
    if not head or not head.next:
        return False
        
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next          # Moves 1 step
        fast = fast.next.next     # Moves 2 steps
        
        if slow == fast:
            return True           # They met, so there is a cycle
            
    return False

# --- Test Cases ---
if __name__ == "__main__":
    # 1 -> 2 -> 3 -> 4 -> points back to 2
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2 # Cycle
    
    print(f"Has Cycle: {has_cycle(node1)}")
