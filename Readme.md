# 📈 Stock Portfolio Tracker — Python

A simple **Stock Portfolio Tracker** written in Python for the **CodeAlpha Python Programming Internship (Task 3)**.

The user enters a **stock name** and **quantity**, and the program calculates the **investment value** using a **hardcoded dictionary of stock prices**. At the end it shows the **total investment** and saves a report in a **`.txt` file**.

---

## 📌 Project Info

| | |
|---|---|
| **Task** | Stock Portfolio Tracker |
| **Domain** | Python Programming |
| **Organisation** | CodeAlpha |
| **Repo name** | `CodeAlpha_StockPortfolioTracker` |
| **Language** | Python 3 |
| **Type** | Console app with file handling |

---

## ✨ Features

- 💹 **Hardcoded price dictionary** — no internet, no API needed:
  ```python
  stock_price = {"AAPL": 180, "TSLA": 250, "TCS": 450,
                 "GOOGL": 150, "MSFT": 400, "AMZN": 190}
  ```
- 📋 Shows the **list of available stocks with prices** at the start
- ⌨️ User types a **stock name + quantity**, and can add as many stocks as they want
- 🔠 `.upper()` and `.strip()` are used, so `aapl`, `AAPL` and ` aapl ` all work
- 🚫 **Wrong stock name** → polite message and asks again (no crash)
- 🛡️ **`try-except` protection** → typing letters instead of a number shows
  *"Please enter a valid number"* instead of a red error
- 🔢 Quantity must be **greater than zero**
- 🧾 **Portfolio table** is shown after every entry, so the user always sees the current holdings
- 💰 **Total investment** is calculated with `price × quantity` and `+=`
- 💾 Report saved automatically in **`portfolio.txt`** using `with open(...)`
- 🏁 Typing **`done`** finishes the program and writes the final report

---

## ▶️ How to Run

**1. Check that Python is installed:**

```bash
python --version
```

**2. Run the program:**

```bash
python stock_tracker.py
```

> On Mac / Linux use `python3 stock_tracker.py`
> No extra library is needed — file handling is built into Python.

---

## 🕹️ How to Use

1. The program shows the available stocks and their prices.
2. Type a stock name, e.g. `AAPL`.
3. Type how many shares, e.g. `10`.
4. The stock is added and the portfolio table is printed.
5. Repeat for more stocks.
6. Type **`done`** to finish → total investment is shown and `portfolio.txt` is saved.

**Available stocks:** `AAPL`, `TSLA`, `TCS`, `GOOGL`, `MSFT`, `AMZN`

---

## 🖥️ Sample Output

```
=========================================
         Stock Portfolio Tracker
=========================================

Available Stocks:
AAPL : 180
TSLA : 250
TCS : 450
GOOGL : 150
MSFT : 400
AMZN : 190

Type 'done' when you finish.

Enter stock name: AAPL
Enter quantity: 10

Investment added successfully!

============= Your Portfolio =============
AAPL | Price: 180 | Quantity: 10 | Value: 1800

Enter stock name: TSLA
Enter quantity: 5

Investment added successfully!

============= Your Portfolio =============
AAPL | Price: 180 | Quantity: 10 | Value: 1800
TSLA | Price: 250 | Quantity: 5 | Value: 1250

Enter stock name: done

Total Investment: 3050

Portfolio saved in portfolio.txt
Thank you for using Stock Portfolio Tracker!
```

**Saved file — `portfolio.txt`**

```
       Stock Portfolio Report
====================================
AAPL | Price: 180 | Quantity: 10 | Value: 1800
TSLA | Price: 250 | Quantity: 5 | Value: 1250

Total Investment: 3050
```

---

## 🧠 Python Concepts Used

| Concept | Where it is used |
|---|---|
| **Dictionary** | `stock_price` stores `stock name → price`; `price = stock_price[stock_name]` gets the price |
| **`.items()`** | `for stock, price in stock_price.items()` prints the whole price list |
| **List** | `Portfolio` list stores every purchase |
| **Tuple** | `(stock_name, price, quantity, investment)` is stored in the list — the 4 values stay together |
| **Input / Output** | `input()` for stock name and quantity, `print()` for the tables |
| **Basic arithmetic** | `investment = price * quantity` and `total_investment += investment` |
| **`+=` operator** | Short form of `total_investment = total_investment + investment` |
| **`while True` + `break`** | Keeps taking input until the user types `done` |
| **`try-except ValueError`** | Stops the program from crashing if quantity is not a number |
| **`int()`** | Converts the typed text into a number for maths |
| **`in` / `not in`** | `if stock_name not in stock_price` checks the stock exists |
| **File handling** | `with open("portfolio.txt", "w") as file:` and `file.write(...)` |
| **f-strings** | `f"{stock_name} | Price: {price}"` puts variables inside text neatly |

---

## 📂 Code Structure

```
CodeAlpha_StockPortfolioTracker/
│
├── Stock_Portfolio_Tracker.py  → the complete program (single file)
├── portfolio.txt               → report created automatically when you run it
└── README.md                   → this file
```

**How the code flows:**

| Step | Line idea | Work |
|---|---|---|
| 1 | `stock_price = {...}` | The hardcoded dictionary of prices |
| 2 | `Portfolio = []`, `total_investment = 0` | Memory for purchases and the running total |
| 3 | `for stock, price in stock_price.items()` | Shows all available stocks |
| 4 | `while True:` | Program keeps asking for stocks |
| 5 | `stock_name = input(...).upper().strip()` | Takes the name, cleans it, makes it capitals |
| 6 | `if stock_name == "DONE": break` | Ends the loop |
| 7 | `if stock_name not in stock_price` | Blocks unknown stock names |
| 8 | `try: quantity = int(input(...))` | Takes quantity safely; `except ValueError` catches text |
| 9 | `investment = price * quantity` | The main maths |
| 10 | `total_investment += investment` | Adds to the running total |
| 11 | `Portfolio.append((...))` | Saves the purchase as a tuple |
| 12 | `for ... in Portfolio: print(...)` | Shows the portfolio table |
| 13 | `with open("portfolio.txt", "w") as file:` | Writes the final report to a file |

---

## 🔍 Understanding the main logic

```python
stock_price = {"AAPL": 180, "TSLA": 250}
```
This is a **dictionary**. Curly brackets `{ }` mean dictionary, and it works like a
small table: the **key** is the stock name, the **value** is its price.
`stock_price["AAPL"]` gives `180`. The task asks for **hardcoded** prices, so no
internet or API is used.

```python
for stock, price in stock_price.items():
    print(stock, ":", price)
```
`.items()` gives both the key and the value together, so we can print the whole
price list in just two lines.

```python
stock_name = input("\nEnter stock name: ").upper().strip()
```
`.upper()` makes `aapl` into `AAPL` so it matches the dictionary.
`.strip()` removes extra spaces if the user types ` AAPL `.

```python
if stock_name not in stock_price:
    print("That stock is not available. Please try again.")
    continue
```
`not in` checks the dictionary. If the stock does not exist, the message is shown
and `continue` skips the rest of the loop, so the user can try again.

```python
try:
    quantity = int(input("Enter quantity: "))
    if quantity <= 0:
        print("Quantity must be greater than zero.")
        continue
except ValueError:
    print("Please enter a valid number.")
    continue
```
`int()` converts text into a number. If the user types `abc`, `int()` fails and
Python raises a `ValueError` — the `except` block catches it and shows a friendly
message **instead of crashing**. This is called **error handling** and it is a
very good habit in every project.

```python
investment = price * quantity
total_investment += investment
```
`price` comes from the dictionary and `quantity` from the user.
`price × quantity` = value of that stock. `+=` adds it to the running total.

```python
Portfolio.append((stock_name, price, quantity, investment))
```
A **tuple** `( )` keeps the 4 values of one purchase together, and `append()` adds
it to the list. So `Portfolio` becomes a small table — one tuple per purchase.

```python
for stock_name, price, quantity, investment in Portfolio:
    print(stock_name, "| Price:", price, "| Quantity:", quantity, "| Value:", investment)
```
This "unpacks" each tuple back into 4 variables and prints one clean line per stock.

```python
with open("portfolio.txt", "w") as file:
    file.write(f"{stock_name} | Price: {price} | Quantity: {quantity} | Value: {investment}\n")
```
**File handling** — the optional part of the task:
- `"w"` means **write** mode (creates a new file)
- `with` closes the file automatically when the block ends (safer than `close()`)
- `f"..."` is an **f-string**: variables inside `{ }` are replaced by their values
- `"\n"` means "go to the next line"

---

## 🚀 Future Improvements (ideas)

- Move the portfolio table **outside** the `while` loop so it prints one final
  summary instead of repeating after every entry
- Save the report as **`.csv`** too, so it opens directly in Excel (`import csv`)
- Fetch **live prices** using an API like `yfinance`
- Show **profit / loss** by storing a buy price and comparing it with the current price
- Add a **budget limit** and warn the user when it is crossed
- Draw a **pie chart** of the portfolio with `matplotlib`
- Use lowercase `portfolio` for the list name (Python style: normal variables are lowercase)

---

## 👩‍💻 Author

**Smeet Jariwala**
Python Programming Intern @ CodeAlpha
📧 smeetjariwala17@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/smeet-jariwala-98b0043a5?utm_source=share_via&utm_content=profile&utm_medium=member_android)

---

## 📜 Acknowledgement

Built as part of the **Python Programming Internship** at
[CodeAlpha](https://www.codealpha.tech) — www.codealpha.tech

⭐ If you liked this project, please give this repository a star!