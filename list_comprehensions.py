# takes this list a and make a new list that has only the even elements
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

new_a = []

for i in range(len(a)):
    if a[i] % 2 == 0:
        new_a.append(a[i])

print(new_a)
