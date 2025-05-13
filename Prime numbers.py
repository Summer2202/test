def is_prime(n):
    """Check if a number is prime using count-controlled iteration"""
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for divisor in range(3, max_divisor, 2): 
        if n % divisor == 0:
            return False
    return True
while True:
    user_input = input("Enter an integer: ")
    
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    try:
        number = int(user_input)
        if is_prime(number):
            print(f"{number} is a prime number!")
        else:
            if number < 2:
                print(f"{number} is not prime (primes are ≥ 2)")
            else:
                print(f"{number} is not prime (divisible by other numbers besides 1 and itself)")
    except ValueError:
        print("Please enter a valid integer or 'quit' to exit")
