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
    "AAPL" : 180,
    "TSLA" : 250,
    "TCS"  : 450,
    "GOOL" : 150,
    "MSFT" : 400,
    "AMZN" : 190
}

portfolio = []

total_inverstment = 0

print("=========================================")
print("         Stock Portfolio Tracker         ")
print("=========================================")

print("\nAvailable Stock : ")

for stock,price in stock_price.items():
    print(stock , ": " ,price)

print("\n'DONE' when you finish.")

while True:

    stock_name = input("\nEnter Stock name :- ").upper().strip()

    if stock_name == "DONE":
        break

    if stock_name not in stock_price:
        print("\nThis Stock is not avaliable. please try again.")
        continue

    try:
        quantity = int(input("\nEnter quantity : "))

        if quantity <= 0:
            print("quantity must be greater than zero.")
            continue
    except ValueError:
        print("\nEnter valid value :- ")
        continue

    price = stock_price[stock_name]

    investment = price * quantity

    total_inverstment = total_inverstment + investment

    portfolio.append(
        stock , price , quantity , investment 
        )

    print("\ninvestment added successfully! ")

    print("\n============================== your portfolio ==============================")

    for stock , price , quantity , investment in portfolio:
        print (
            stock,
            "| price : "     , price,
            "| quantity : " , quantity,
            "| value :"      , investment
        )        

    print("\nTotal inverstment : " ,total_inverstment)

with open("Portfolio.txt" , "w") as file:
    file.write("        Stock portfolio report        \n")
    file.write("========================================")

    for stock, price, quantity, investment in portfolio:
        file.write(
            f"stock : {stock_name} | price : {price}"
            f"quantity : {quantity} | value : {investment}\n" 
        )

        file.write(
            f"Total Inverstment : {total_inverstment}\n"
        )

    print("\nsave 'portfolio.txt' file successfully.")
    print("Thank you for using Stock portfolio tracker!")