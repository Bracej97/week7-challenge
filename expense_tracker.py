import requests

base_url = "http://127.0.0.1:3000/expenses"

def view_expenses():
    expenses_json = requests.get(base_url)
    print(expenses_json)
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

if __name__ == '__main__':
    view_expenses()
