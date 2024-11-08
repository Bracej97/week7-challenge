# Import all the required functionality
import unittest
from unittest.mock import patch
import sys
import os
import json


# Add the parent directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from expense_tracker import *

# Create sample expense data to use in testing
sample_simple_expense = [{'description': 'lunch', 'amount': 10.5, 'date': "28-08-1997", 'id': 1}]

sample_multiple_expense = [
    {'description': 'lunch', 'amount': 10.5, 'date': "28-08-1997", 'id': 1},
    {'description': 'dinner', 'amount': 30.75, 'date': "07-11-2024", 'id': 2},
    {'description': 'breakfast', 'amount': 5, 'date': "04-11-2024", 'id': 3}
]


# Test class for expense tracker
class TestExpenseTracker(unittest.TestCase):
    # Testing the view expense function with mocked API response for GET for single and multiple expenses
    @patch('requests.get')
    def test_view_expenses(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'expenses': sample_simple_expense}

        data = view_expenses()

        assert data[0]['description'] == 'lunch'
        assert data[0]['amount'] == 10.5
        assert data[0]['date'] == "28-08-1997"
        mock_get.assert_called_once()

    @patch('requests.get')
    def test_view_expenses_multiple(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'expenses': sample_multiple_expense}

        data = view_expenses()

        assert data[0]['description'] == 'lunch'
        assert data[0]['amount'] == 10.5
        assert data[0]['date'] == "28-08-1997"
        assert data[1]['description'] == 'dinner'
        assert data[1]['amount'] == 30.75
        assert data[1]['date'] == "07-11-2024"
        assert data[2]['description'] == 'breakfast'
        assert data[2]['amount'] == 5
        assert data[2]['date'] == "04-11-2024"
        mock_get.assert_called_once()

    # Testing the add expense function with a mocked API response for the POST request
    @patch('requests.post')
    def test_add_expense(self, mock_post):
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = sample_simple_expense

        data = add_expense(sample_simple_expense)

        assert data[0]['description'] == 'lunch'
        assert data[0]['amount'] == 10.5
        assert data[0]['date'] == "28-08-1997"
        mock_post.assert_called_once()

    # Testing the update expense function with a mocked API response for the PUT request
    @patch('requests.put')
    def test_update_expense(self, mock_put):
        expense_id = 1
        mock_put.return_value.status_code = 200
        mock_put.return_value.json.return_value = sample_simple_expense

        data = update_expense(expense_id, sample_simple_expense)

        assert data[0]['description'] == 'lunch'
        assert data[0]['amount'] == 10.5
        assert data[0]['date'] == "28-08-1997"
        mock_put.assert_called_once()

    # Testing the update expense function failing with a mocked API response for the PUT request
    @patch('requests.put')
    def test_update_expense_not_found(self, mock_put):
        expense_id = 1
        mock_put.return_value.status_code = 404
        mock_put.return_value.json.return_value = {'error': 'Expense not found'}

        data = update_expense(expense_id, sample_simple_expense)

        self.assertEqual(data, 'Expense not found')
        mock_put.assert_called_once()

    # Testing the delete expense function with a mocked API response for the DELETE request
    @patch('requests.delete')
    def test_delete_expense(self, mock_delete):
        expense_id = 1
        mock_delete.return_value.status_code = 204

        data = delete_expense(expense_id)

        self.assertEqual(data, 204)
        mock_delete.assert_called_once()
