def factorial_recursive(n: int) -> int:
    """
    Calculates the factorial of a number using recursion.
    
    Time Complexity: O(n) - n recursive calls.
    Space Complexity: O(n) - Call stack takes up n space.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Calculates the factorial of a number iteratively.
    
    Time Complexity: O(n) - Loop runs n times.
    Space Complexity: O(1) - Only a single variable is used.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# --- Test Cases ---
if __name__ == "__main__":
    print("--- Recursive ---")
    print(f"factorial(5) -> {factorial_recursive(5)}")
    print(f"factorial(0) -> {factorial_recursive(0)}")
    
    print("\n--- Iterative ---")
    print(f"factorial(5) -> {factorial_iterative(5)}")
    print(f"factorial(0) -> {factorial_iterative(0)}")
