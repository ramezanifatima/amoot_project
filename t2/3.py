fruits = ['orange', 'apple', 'pineapple', 'coconut', 'cantaloupe']
new_list = []
le = len(fruits) * -1
for item in range(-1, le-1, -1):
    new_list.append(fruits[item])

print(fruits)
print(new_list)