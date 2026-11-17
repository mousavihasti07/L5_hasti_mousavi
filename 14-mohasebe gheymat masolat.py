products = [
("Laptop", 50000, 2),
("Mouse", 800, 3),
("Keyboard", 1500, 2),
("Monitor", 12000, 1)]
total_price = 0

for product,price,number in products:
    product_price = price * number
    total_price= product_price + total_price
    
print(f'the final price is: {total_price}')


