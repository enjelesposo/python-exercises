num = int(input("Please enter a number: "))

if num % 4 == 0:
    print(str(num) + " is divisible by 4.")
elif num % 2 == 0:
    print(str(num) + " is an even number.")
else:
    print(str(num) + " is an odd number.")
