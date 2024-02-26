import math

def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n (int): The number for which factorial is to be calculated.

    Returns:
        int: The factorial of the input number.

    Raises:
        ValueError: If the input number is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(n)

def main():
    """
    Main function to prompt user input for a number and calculate its factorial.
    """
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Factorial is not defined for negative numbers")
        else:
            result = factorial(num)
            print("Factorial of", num, "is", result)
    except ValueError as ve:
        print("Error: Invalid input. Please enter a valid non-negative integer.")

if __name__ == "__main__":
    main()
