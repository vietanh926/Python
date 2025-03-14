lower_letter = ['a','c','v','d','s','f']
upper_letter = [i.upper() for i in lower_letter]
print(upper_letter)



original_price = [3.12,-1,12.12,13.4,-2.1]

price = [i if i>0 else 0 for i in original_price]
print(price)



fruit = ['apple','orange','banana','watermelon','cherry','strawberry']

fruit_with_a = [i for i in fruit if 'a' in i]
print(fruit_with_a)


odd_square = [i**2 for i in range(1,10) if i %2!=0]
print(odd_square)