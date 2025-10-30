
import pandas as pd

data = {' Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)
df.rename(columns={
    "Name":"Name",
    "Age":"age"
},inplace=True)
print(df)


print(df.head(3))

mean_age=df["age"].mean()
print(mean_age)


print(df[["Name", "City"]])


df["Salary"]=150
print(df)


print(df.describe())

import pandas as pd


data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [5000, 6000, 7500, 8000],
    "Expenses": [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(data)


print(sales_and_expenses)


print(sales_and_expenses[["Sales","Expenses"]].max())


print(sales_and_expenses[["Sales","Expenses"]].min())

print(sales_and_expenses[["Sales","Expenses"]].mean())

import pandas as pd


data = {
    "Category": ["Rent", "Utilities", "Groceries", "Entertainment"],
    "January": [1200, 200, 300, 150],
    "February": [1300, 220, 320, 160],
    "March": [1400, 240, 330, 170],
    "April": [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)

print(expenses)

expenses=expenses.set_index('Category')
max_expense=expenses.max(axis=1)
print(max_expense)

min_expense=expenses.min(axis=1)
print(min_expense)

avg_expense=expenses.mean(axis=1)
print(avg_expense)
