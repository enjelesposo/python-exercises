# create a function that reverses a string
def reverse(str):
    x = ''
    for i in range(len(str) - 1, -1, -1):
        x += str[i]
    return x


# Ask user for string
str = input("Please enter a string... ")
mod_str = str.lower().replace(" ", "")

# reverse the string
str_reverse = reverse(mod_str)

# compare the original string to the reversed string
if (mod_str == str_reverse):
    print(str + " is a palidrome.")
else:
    print(str + " is not a palidrome.")
