def check_weird(n):
    if n % 2 == 1:  # If n is odd
        print("Weird")
    elif 2 <= n <= 5:  # If n is even and in the range [2, 5]
        print("Not Weird")
    elif 6 <= n <= 20:  # If n is even and in the range [6, 20]
        print("Weird")
    else:  # If n is even and greater than 20
        print("Not Weird")

# Read input
n = int(input().strip())  # Read an integer from input
check_weird(n)  # Call the function
