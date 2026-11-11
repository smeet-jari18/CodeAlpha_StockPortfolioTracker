'''

TASK 3: Stock Portfolio Tracker
● Goal: Build a simple stock tracker that calculates total investment based on manually defined stock
prices.
● Simplified Scope:
○ User inputs stock names and quantity.
○ Use a hardcoded dictionary to define stock prices (e.g., {"AAPL": 180, "TSLA": 250}).
○ Display total investment value and optionally save the result in a .txt or .csv file.
● Key Concepts Used: dictionary, input/output, basic arithmetic, file handling
(optional).

'''


stock_price = {
    "AAPL": 180,
    "TSLA": 250,
    "TCS": 450,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 190
}

Portfolio = []

total_investment = 0

print("=========================================")
print("         Stock Portfolio Tracker         ")
print("=========================================")

print("\nAvailable Stocks:")

for stock, price in stock_price.items():
    print(stock, ":", price)

print("\nType 'done' when you finish.")

while True:

    stock_name = input("\nEnter stock name: ").upper().strip()

    
    if stock_name == "DONE":
        break

    
    if stock_name not in stock_price:
        print("That stock is not available. Please try again.")
        continue

    
    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    
    price = stock_price[stock_name]

    investment = price * quantity

    total_investment += investment

    
    Portfolio.append(
        (stock_name, price, quantity, investment)
    )

    print("\nInvestment added successfully!")

    
    print("\n============= Your Portfolio =============")

    for stock_name, price, quantity, investment in Portfolio:
        print(
            stock_name,
            "| Price:", price,
            "| Quantity:", quantity,
            "| Value:", investment
        )


print("\nTotal Investment:", total_investment)


with open("portfolio.txt", "w") as file:

    file.write("       Stock Portfolio Report\n")
    file.write("====================================\n")

    for stock_name, price, quantity, investment in Portfolio:

        file.write(
            f"{stock_name} | Price: {price} | "
            f"Quantity: {quantity} | Value: {investment}\n"
        )

    file.write(
        f"\nTotal Investment: {total_investment}\n"
    )

print("\nPortfolio saved in portfolio.txt")
print("Thank you for using Stock Portfolio Tracker!")