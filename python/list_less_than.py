arr = [1, 6, 8, 2, 3, 5, 41, 12, 4, 9, 15, 2, 3, 78, 51]
new_arr = []

# iterate through arr (i is arr[i])
for i in arr:
    # check if i is less than 10
    if i < 10:
        new_arr.append(i)

print(sorted(new_arr))
