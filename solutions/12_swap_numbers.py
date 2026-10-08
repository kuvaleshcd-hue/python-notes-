def swap_numbers(a: int, b: int) -> tuple[int, int]:
    """
    Swaps two numbers without using a temporary variable.
    Python has a built-in tuple unpacking method, but we also show the math way.
    """
    # 1. Pythonic Way (Tuple Unpacking)
    a, b = b, a
    return a, b

def swap_math(a: int, b: int) -> tuple[int, int]:
    """Swap using arithmetic (addition and subtraction)"""
    a = a + b
    b = a - b
    a = a - b
    return a, b
    
def swap_xor(a: int, b: int) -> tuple[int, int]:
    """Swap using Bitwise XOR (best for integers)"""
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

# --- Test Cases ---
if __name__ == "__main__":
    x, y = 5, 10
    print(f"Original: x={x}, y={y}")
    x, y = swap_xor(x, y)
    print(f"Swapped: x={x}, y={y}")
