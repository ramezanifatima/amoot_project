fruit = ['apple', 'banana', 'orange']
favorite_fruit = input('Enter your favorite fruit')
if favorite_fruit in fruit:
    print('This fruit is available in the list')
else:
    fruit.append(favorite_fruit)

print(fruit)
