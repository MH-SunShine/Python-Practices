products = []
total_price = 0

while True:
    product = input("enter the product name - ('done' to exit):")
    if product == "done":
        break
    else:
        products.append(product)
        price = float(input("enter the product price:"))
        total_price += price

print("===== your shopping chart =====")
product_number = 1
for product in products:
    print(f"{product_number} - {product} - {price}")
    product_number += 1
print(f"total price = {total_price}")