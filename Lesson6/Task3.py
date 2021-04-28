i = tuple(range(1, 11))
j = tuple([x**2 for x in i])
v = [i, j]


list = [[row[i] for row in v] for i in range(len(i))]

new_list = tuple(list)

print(new_list)



