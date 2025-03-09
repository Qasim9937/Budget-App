# Budget Category and Spending Chart

## Overview
This project provides a `Category` class for managing budgets and a `create_spend_chart` function for visualizing spending across different categories.

## Features
- **Category Management**: Deposit, withdraw, and transfer funds between categories.
- **Ledger Tracking**: Keeps a record of transactions with descriptions.
- **Balance Checking**: Ensures sufficient funds before withdrawal or transfer.
- **Spending Visualization**: Generates a bar chart showing spending percentages across categories.

## Class: `Category`
### Methods:

#### `__init__(self, category, bal=0)`
- Initializes a category with a name and optional starting balance.
- Parameters:
  - `category` (str): The name of the budget category.
  - `bal` (float, optional): Initial balance (default is 0).

#### `__str__(self)`
- Returns a formatted string representing the category's transactions and total balance.

#### `deposit(self, amount, description='')`
- Adds funds to the category.
- Parameters:
  - `amount` (float): The amount to deposit.
  - `description` (str, optional): A description of the deposit.

#### `withdraw(self, amount, description='')`
- Deducts funds if sufficient balance is available.
- Parameters:
  - `amount` (float): The amount to withdraw.
  - `description` (str, optional): A description of the withdrawal.
- Returns:
  - `True` if successful, `False` otherwise.

#### `get_balance(self)`
- Returns the current balance of the category.

#### `transfer(self, amount, destination)`
- Transfers funds to another `Category` object if sufficient funds are available.
- Parameters:
  - `amount` (float): The amount to transfer.
  - `destination` (`Category`): The category to transfer funds to.
- Returns:
  - `True` if successful, `False` otherwise.

#### `check_funds(self, amount)`
- Checks if the category has enough funds for a transaction.
- Parameters:
  - `amount` (float): The amount to check.
- Returns:
  - `True` if sufficient funds are available, `False` otherwise.

---

## Function: `create_spend_chart(categories)`
### Description
Generates a textual bar chart showing the percentage of spending for each category.

### Parameters:
- `categories` (list of `Category` objects): The budget categories to include in the chart.

### Output Format:
The chart displays spending percentages in increments of 10%, with categories listed below:
```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60|       o  
 50|       o  
 40|       o  
 30|    o  o  
 20|    o  o  
 10|    o  o  
  0| o  o  o  
    ----------
     F  E  D  
     o  u  u  
     o  c  c  
     d  a  a  
        t  t  
        i  i  
        o  o  
        n  n  
```

### Example Usage:
```python
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(1000, "Initial deposit")
food.withdraw(300, "Groceries")
entertainment.deposit(500, "Initial deposit")
entertainment.withdraw(200, "Movies")
business.deposit(800, "Initial deposit")
business.withdraw(400, "Office Supplies")

print(create_spend_chart([food, entertainment, business]))
```

## Conclusion
This project provides an easy way to manage budget categories and visualize spending through a textual chart.

