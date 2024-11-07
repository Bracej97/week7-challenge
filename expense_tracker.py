import requests

base_url = "http://localhost:5000/expenses"

def view_expenses():
    expenses_requested = requests.get(base_url)
    if expenses_requested.status_code == 200:
        expenses_json = expenses_requested.json()
        print(expenses_json)
        #expenses = expenses_json['expenses']
        for expense in expenses_json:
            print(f"""
                  Description: {expense['description']}
                  Amount: {expense['amount']}
                  Date: {expense['date']}
                  """)
            return expense

    else:
        print("Error retrieving expenses: ", expenses_json.status_code)
