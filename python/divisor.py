# create a list using ranges
num = int(input("Enter a number: "))

arr = range(2, num)
new_arr = []

for d in arr:
    if(num % d == 0):
        new_arr.append(d)

print("Divisors of " + str(num) + ": ")
print(new_arr)
