# Programmer: Gavin Huggins
# Description: # Ask the user for how many items bought and calculate total

#Ask user for items # and cost
items = float(input("How many items are you purchasing? "))
while items < 0:
    print("Invalid item number, Try again!")
    items = int(input("How many items are you purchasing? "))
item_count = 1
subtotal = 0.0
while item_count <= items:
    cost = float(input(f"Enter item {item_count} price: "))
    while cost < 0:
        print("Invalid cost, Try again!")
        cost = float(input(f"Enter item {item_count} price: "))
    subtotal += cost
    item_count += 1

# Calculate and print Subtotal, Tax, and Total
print(f"Subtotal: ${subtotal:,.2f}")
tax = subtotal * 0.13
print(f"Tax: ${tax:,.2f}")
total = subtotal + tax
print(f"Total: ${total:,.2f}")

