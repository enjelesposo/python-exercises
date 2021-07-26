# Write a program which can compute the factorial of a given numbers.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

num = int(input("Enter a number and I will tell you it's factorial: "))


def computeFactorial(num):
    num = num
    for i in range(1, num):
        num = num * i

    return num


print(computeFactorial(num))
