products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for price in products.values():
    print(price)

print("")    

for product in products:
    print(product)

print("")

for product in products.items():
    print(product)

for product, price in products.items():
    print(product, price)

print("")

for product, price in products.items():
    products[product] = round(price * 0.8)
    print(products)