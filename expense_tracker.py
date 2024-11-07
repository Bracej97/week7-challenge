import requests

base_url = "http://localhost:5000/expenses"

def view_expenses():
    expenses_json = requests.get(base_url)
    if expenses_json.status_code == 200:
        expenses = expenses_json.json()

        for expense in expenses:
            print(f"""
                  Description: {expense['description']}
                  Amount: {expense['amount']}
                  Date: {expense['date']}
                  """)
        return expenses
    else:
        print("Error retrieving expenses: ", expenses_json.status_code)
