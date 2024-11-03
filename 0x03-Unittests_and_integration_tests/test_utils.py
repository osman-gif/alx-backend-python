#!/usr/bin/env python3
"""
Familiarize yourself with the utils.access_nested_map function and understand
its purpose. Play with it in the Python console to make sure you understand.

In this task you will write the first unit test for utils.access_nested_map.

Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to test that
the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function for
following inputs:

nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")

"""
import unittest
from parameterized import parameterized
from utils import access_nested_map  # Import the function you're testing


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns the expected result for
        various inputs."""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """raises KeyError with appropriate message for missing keys."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Check if the KeyError message matches the missing key
        missing_key = path[-1]
        self.assertEqual(str(context.exception), f"'{missing_key}'")


if __name__ == '__main__':
    unittest.main()
