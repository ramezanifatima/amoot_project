inventory = {
    'peach': {
        'price': 20,
        'stock': 10
    },
    'blueberry': {
        'price': 50,
        'stock': 15
    },
    'pineapple': {
        'price': 50,
        'stock': 5
    },
    'banana': {
        'price': 80,
        'stock': 10
    }
}
shopping_list = {}
total_cost = 0
while True:
    item = input('Enter your shopping list  : ')
    if item == '':
        break
    quantities = int(input('Specify the number of selected items for purchase  : '))
    shopping_list.update({item: quantities})

for item in shopping_list:
    if item in inventory:
        i = inventory[item]
        stock = i['stock']
        if stock < shopping_list[item]:
            print('The desired quantity is not available in the warehouse')
        else:
            i['stock'] = stock - shopping_list[item]
            price = i['price'] * shopping_list[item]
            total_cost += price

    else:
        print(f'The {item} item is not available for purchase')

print(f' total cast {total_cost} \n new inventory ------> {inventory}')
