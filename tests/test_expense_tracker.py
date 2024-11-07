import unittest
from unittest.mock import patch
import requests
import sys
import os


# Add the parent directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from expense_tracker import *

class TestExpenseTracker(unittest.TestCase):

    @patch('requests.get')
    def test_view_expenses(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'description': 'lunch', 'amount': 10.5, 'date': "28-08-1997"}]

        data = view_expenses()

        assert data[0]['description'] == 'lunch'
        assert data[0]['amount'] == 10.5
        assert data[0]['date'] == "28-08-1997"

    @patch('requests.get')
    def test_view_expenses_multiple(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {'description': 'lunch', 'amount': 10.5, 'date': "28-08-1997"},
            {'description': 'dinner', 'amount': 30.75, 'date': "07-11-2024"},
            {'description': 'breakfast', 'amount': 5, 'date': "04-11-2024"}
            ]

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
