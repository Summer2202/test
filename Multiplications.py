while True:
    try:
        number = int(input("Enter a number: "))
        if number > 0:
            print(f"Multiplication table for {number}:")
            for num in range(1, 13):
                print(f"{number} x {num} = {number * num}")
            break 
        else:
            print("Not a positive integer.")
    except ValueError:
        print("Please enter a valid positive integer.")
