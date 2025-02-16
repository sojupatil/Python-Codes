# Stock price comparison using Dictionary
nse = {
    "first": {"name": input("Enter name of first stock: "), "price": int(input("Enter price of first stock: "))},
    "second": {"name": input("Enter name of second stock: "), "price": int(input("Enter price of second stock: "))}
}

# Compare prices
if nse["first"]["price"] > nse["second"]["price"]:
    print("First stock is greater than second")
else:
    print("Second stock is greater than first")

#------------------------------------------------------------------------

# Stock price comparison using Tuple
bse = (
    input("Enter name of first stock (Tuple): "), int(input("Enter price of first stock (Tuple): ")),
    input("Enter name of second stock (Tuple): "), int(input("Enter price of second stock (Tuple): "))
)

print("First stock:", bse[0], "Price:", bse[1])

# Compare prices
if bse[1] > bse[3]:
    print("First stock is greater than second")
else:
    print("Second stock is greater than first")

#------------------------------------------------------------------------

# Stock price comparison using List
nsme = [
    input("Enter name of first stock (List): "), int(input("Enter price of first stock (List): ")),
    input("Enter name of second stock (List): "), int(input("Enter price of second stock (List): "))
]

print("First stock:", nsme[0])

# Compare prices
if nsme[1] > nsme[3]:
    print("First stock price is greater")
else:
    print("Second stock price is greater")
