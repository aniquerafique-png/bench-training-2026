while True:
    number = int(input("Enter a number (1-12): "))

    if 1 <= number <= 12:
        print(f"\nMultiplication Table for {number}\n")

        for i in range(1, 13):
            print(f"{number:>2} x {i:>2} = {number*i:>3}")

        break
    else:
        print("Invalid number. Please try again.")