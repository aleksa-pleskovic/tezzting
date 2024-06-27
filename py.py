# This script contains intentional code smells and issues

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def find_max(arr):
    max_val = -9999999
    for i in arr:
        if i > max_val:
            max_val = i
    return max_val

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main():
    # Calculate factorial of 5
    fact = calculate_factorial(5)
    print(f"Factorial of 5 is: {fact}")

    # Find the maximum in the list
    numbers = [1, 2, 3, 4, 5, -100, 9999999]
    max_num = find_max(numbers)
    print(f"Maximum number in the list is: {max_num}")

    # Check if a number is prime
    prime_status = is_prime(17)
    print(f"Is 17 a prime number? {'Yes' if prime_status else 'No'}")

    # Example of unused variable
    unused_var = 12345

if __name__ == "__main__":
    main()
