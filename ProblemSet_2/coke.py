amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    val = int(input("Insert Coin: "))
    if val not in [5, 10, 25]:
        print("Invalid coin. Please insert a valid coin.")
        continue
    amount_due -= val

print(f"Change Owed: {abs(amount_due)}")
