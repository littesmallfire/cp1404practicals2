number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
total_price=0
for i in range(0, number_of_items):
    price = float(input("Price of item: "))
    total_price += price
if total_price > 100:
    discounted_price = total_price - (total_price*0.1)
    print(f"Total price for {number_of_items} is ${discounted_price:.2f}.")
else:
    print(f"Total price for {number_of_items} is ${total_price}.")