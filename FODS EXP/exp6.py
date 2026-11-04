price = [100, 200, 300]
qty = [2, 1, 3]

total = sum(price[i] * qty[i] for i in range(3))

discount = total * 10 / 100
amount = total - discount
tax = amount * 5 / 100

print("Final cost:", amount + tax)
