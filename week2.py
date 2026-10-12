# Step 1: Ask the user for the price of one item and the quantity
price_input = input("Enter the price of one item: ")
quantity_input = input("Enter the quantity they want: ")

# Step 2: Convert input strings to float (for price) and int (for quantity)
price = float(price_input)
quantity = int(quantity_input)

# Step 3: Calculate the total
total = price * quantity

# Step 4: Print a friendly summary using an f-string
print(f"{quantity} items at {price:.2f} each = {total:.2f}")
