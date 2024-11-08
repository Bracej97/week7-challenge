# Import the requests module
import requests

# Set the base URL for calling the API
base_url = "http://127.0.0.1:3000/expenses"

# Create the function to view the expenses
def view_expenses():
    # Call a GET request to the API
    expenses_json = requests.get(base_url)

    # If the API returns a 200 code then access the expenses and iterate through them printing the expenses
    # Returns the error code if not 200 code returned
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

# Create the function add a new expense
def add_expense(new_expense):
    # Call a POST request to the API with the new expense
    send_expense = requests.post(base_url, json = new_expense)

    # If the API returns a 201 code then the expense has been added succesfully, print message to confirm this
    # If different error code returned then this is printed
    if send_expense.status_code == 201:
        print("Expense has been added!")
        return send_expense.json()
    else:
        print("Error adding expense: ", send_expense.status_code)

# Create the function to update an expense
def update_expense(expense_id, updated_data):
    # Call a PUT request to the API with the updated expense and the ID of the expense to update
    send_updated_expense = requests.put(f'{base_url}/{expense_id}', json = updated_data)

    # If the API returns a 200 code then the expense has been updated succesfully, print message to confirm this
    # If the API returns a 404 error code then the expense that needs to be updated can't be found
    # If the API returns a different code then this is printed
    if send_updated_expense.status_code == 200:
        print("Expense has been updated!")
        return send_updated_expense.json()
    elif send_updated_expense.status_code == 404:
        error = send_updated_expense.json()['error']
        print(error)
        return error
    else:
        print("Error updating expense: ", send_updated_expense.status_code)

# Create the function to delete an expense
def delete_expense(expense_id):
    # Call a DELETE request to the API with the ID of the expense to delete
    deleted_expense = requests.delete(f'{base_url}/{expense_id}')

    # If the API returns a 204 code then the expense has been deleted succesfully, print message to confirm this
    # If the API returns a different code then this is printed
    if deleted_expense.status_code == 204:
        print("Deleting complete")
        return 204
    else:
        print("Error deleting expense: ", deleted_expense.status_code)

# Create a function to capture the inputs from the user to feed to the functions to interact with the API
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

    # Run the command the user has chosen, capturing extra information if needed
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
