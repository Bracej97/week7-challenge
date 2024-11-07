import requests

base_url = "http://127.0.0.1:3000/expenses"

def view_expenses():
    expenses_json = requests.get(base_url)

    if expenses_json.status_code == 200:
        expenses = expenses_json.json()['expenses']
        print(expenses)

        for expense in expenses:
            print(f"""
                  Description: {expense['description']}
                  Amount: {expense['amount']}
                  Date: {expense['date']}
                  """)
        return expenses
    else:
        print("Error retrieving expenses: ", expenses_json.status_code)

def add_expense(new_expense):
    send_expense = requests.post(base_url, json = new_expense)

    if send_expense.status_code == 201:
        print("Expense has been added!")
        return send_expense.json()
    else:
        print("Error adding expense: ", send_expense.status_code)

if __name__ == '__main__':
    add_expense({'description': 'lunch', 'amount': 10.5, 'date': "28-08-1997"})
