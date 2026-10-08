def generate_fibonacci(n: int) -> list[int]:
    """
    Generates the first n numbers of the Fibonacci series iteratively.
    
    Time Complexity: O(n)
    Space Complexity: O(n) to store the result list.
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
        
    fib_series = [0, 1]
    for _ in range(2, n):
        next_fib = fib_series[-1] + fib_series[-2]
        fib_series.append(next_fib)
        
    return fib_series

# --- Test Cases ---
if __name__ == "__main__":
    print(f"Fibonacci(5): {generate_fibonacci(5)}")
    print(f"Fibonacci(10): {generate_fibonacci(10)}")
