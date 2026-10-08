def fizzbuzz(n: int) -> None:
    """
    Prints the numbers from 1 to n.
    For multiples of 3, print "Fizz".
    For multiples of 5, print "Buzz".
    For multiples of both, print "FizzBuzz".
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# --- Test Cases ---
if __name__ == "__main__":
    print("FizzBuzz up to 15:")
    fizzbuzz(15)
