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
        print(data)

        assert data['description'] == 'lunch'
        assert data['amount'] == 10.5
        assert data['date'] == "28-08-1997"
