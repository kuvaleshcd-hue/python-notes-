import math

def is_prime(n: int) -> bool:
    """
    Checks if a given number is prime using optimized trial division.
    
    Time Complexity: O(sqrt(n))
    Space Complexity: O(1)
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
        
    # Check up to the square root of n
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
            
    return True

# --- Test Cases ---
if __name__ == "__main__":
    print(f"is_prime(11): {is_prime(11)}")
    print(f"is_prime(15): {is_prime(15)}")
    print(f"is_prime(2): {is_prime(2)}")
