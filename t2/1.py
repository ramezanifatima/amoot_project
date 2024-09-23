sum_even_numbers = 0
sum_odd_numbers = 0
for num in range(101):
    if num % 2 == 0:
        sum_even_numbers += num
    else:
        sum_odd_numbers += num

print(f'Sum of positive numbers ----> {sum_even_numbers} \n and \n'
      f'Sum of negative numbers -----> {sum_odd_numbers}')
