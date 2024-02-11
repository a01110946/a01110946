"""
Unit tests for the Customer class.

This module contains tests that verify the functionality of the Customer class,
ensuring that all methods behave as expected under various conditions.
"""

import unittest
import os
import io
from unittest.mock import patch
from bookinn.customer.customer import Customer


class TestCustomer(unittest.TestCase):
    """Tests for functionality of the Customer class."""
    def setUp(self):
        """Setup method to create a customer instance before each test."""
        self.customer = Customer(customer_id=1, name='John Doe', email='johndoe@example.com')

    def test_customer_initialization(self):
        """Test the initialization of a customer."""
        self.assertEqual(self.customer.customer_id, 1)
        self.assertEqual(self.customer.name, 'John Doe')
        self.assertEqual(self.customer.email, 'johndoe@example.com')

    def test_delete_customer(self):
        """Test deleting a customer removes their data file."""
        # Setup: Create a new customer and ensure their data file exists
        customer_id = "cust1001"
        Customer.create_customer(customer_id, "John Doe", "john@example.com")
        expected_filename = f"customer_{customer_id}.json"
        self.assertTrue(os.path.exists(expected_filename), "Customer data file should exist after creation.")

        # Act: Delete the customer
        Customer.delete_customer(customer_id)

        # Assert: Verify the customer's data file has been deleted
        self.assertFalse(os.path.exists(expected_filename), "Customer data file should be deleted.")

    def test_display_customer_info(self):
        """Test displaying customer information prints the correct details."""
        customer = Customer("cust1002", "Jane Doe", "jane@example.com")
        expected_output = "Customer ID: cust1002,\n              Name: Jane Doe, Email: jane@example.com\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            customer.display_customer_info()
            self.assertEqual(fake_out.getvalue(), expected_output,
                             "The output should match the expected customer details.")

    def test_update_details(self):
        """Test updating customer's details."""
        new_name = 'Jane Doe'
        new_email = 'janedoe@example.com'
        self.customer.update_details(name=new_name, email=new_email)
        self.assertEqual(self.customer.name, new_name)
        self.assertEqual(self.customer.email, new_email)

    def test_load_customer(self):
        """Test loading a customer retrieves the correct information."""
        # Setup: Create a customer and write their data to a file
        customer_id = "cust1003"
        original_customer = Customer.create_customer(customer_id, "Bob Smith", "bob@example.com")

        # Act: Load the customer from the file
        loaded_customer = Customer.load_customer(customer_id)

        # Assert: Verify the loaded customer matches the original
        self.assertEqual(loaded_customer.customer_id, original_customer.customer_id, "Customer IDs should match.")
        self.assertEqual(loaded_customer.name, original_customer.name, "Customer names should match.")
        self.assertEqual(loaded_customer.email, original_customer.email, "Customer emails should match.")

        # Cleanup: Delete the customer file to clean up test environment
        os.remove(f"customer_{customer_id}.json")


if __name__ == '__main__':
    unittest.main()
