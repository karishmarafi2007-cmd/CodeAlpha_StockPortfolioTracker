stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 320
}

total_value = 0

print("Available Stocks:")
for stock, price in stock_prices.items():
    print(stock, ":", price)

while True:
    stock_name = input("\nEnter Stock Name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input("Enter Quantity: "))
        investment = stock_prices[stock_name] * quantity
        total_value += investment
        print("Investment Value:", investment)
    else:
        print("Stock not found!")

print("\nTotal Portfolio Value =", total_value)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Portfolio Value = {total_value}")

print("Data saved to portfolio.txt")