def reverse_integer(x):
    # Handle the sign of x
    sign = -1 if x < 0 else 1
    x *= sign
    
    # Reverse the digits of x
    reversedX = 0
    while x > 0:
        reversedX = reversedX * 10 + x % 10
        x //= 10
    
    # Restore the sign
    reversedX *= sign
    
    # Check for overflow
    if reversedX < -2**31 or reversedX > 2**31 - 1:
        return 0
    
    return reversedX

# User-provided example
x = int(input("Enter an integer to reverse: "))
print("Reversed integer is:", reverse_integer(x))

