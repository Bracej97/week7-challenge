import requests

base_url = "http://127.0.0.1:3000/expenses"

def view_expenses():
    expenses_json = requests.get(base_url)

    if expenses_json.status_code == 200:
        expenses = expenses_json.json()['expenses']

        for expense in expenses:
            print(f"""
                  ID: {expense['id']}
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

def update_expense(expense_id, updated_data):
    send_updated_expense = requests.put(f'{base_url}/{expense_id}', json = updated_data)

    if send_updated_expense.status_code == 200:
        print("Expense has been updated!")
        return send_updated_expense.json()
    elif send_updated_expense.status_code == 404:
        error = send_updated_expense.json()['error']
        print(error)
        return error
    else:
        print("Error updating expense: ", send_updated_expense.status_code)

def delete_expense(expense_id):
    deleted_expense = requests.delete(f'{base_url}/{expense_id}')

    if deleted_expense.status_code == 204:
        print("Expense has been deleted")
        return 204
    else:
        print("Failed to delete expense")

def start():
    print("Welcome to your expense tracker. You can:")
    print("""
        [ 1 ] View your expenses
        [ 2 ] Add an expense
        [ 3 ] Edit an expense
        [ 4 ] Delete an expense
        [ 5 ] Exit
        """)

    # Allow the user to input their choice of what they want to do
    try:
        user_choice = int(input("Enter the number for what you want to do: "))
    except ValueError:
        print("You have made an invalid input. Please enter a number between 1 & 5")
        start()

    if user_choice >= 6:
        print("You have made an invalid input. Please enter a number between 1 & 5")
        start()
    # Run the command the user has chosen
    if user_choice == 1:
        view_expenses()
        start()
    if user_choice == 2:
        input_description = input("Description: ")
        input_amount = float(input("Amount: "))
        input_date = input("Date (dd-mm-yyyy): ")
        new_expense = {'description': input_description, 'amount': input_amount, 'date': input_date}
        add_expense(new_expense)
        start()
    if user_choice == 3:
        view_expenses()
        id_to_update = int(input("Enter the ID of the expense you want to edit: "))
        input_description = input("Description: ")
        input_amount = float(input("Amount: "))
        input_date = input("Date (dd-mm-yyyy): ")
        new_expense = {'description': input_description, 'amount': input_amount, 'date': input_date}
        update_expense(id_to_update, new_expense)
        start()
    if user_choice == 4:
        view_expenses()
        id_to_delete = int(input("Enter the ID of the expense you want to delete: "))
        delete_expense(id_to_delete)
        start()
    if user_choice == 5:
        print("Thank you for viewing your expenses.")


if __name__ == '__main__':
    start()
