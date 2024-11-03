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
from unittest.mock import Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


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


class TestGetJson(unittest.TestCase):
    """Test the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json calls requests.get with the correct URL."""

        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):

    def test_memoize(self):
        """Test that memoize caches results correctly."""
        class MyClass:
            def __init__(self):
                self._called = 0

            @memoize
            def a_method(self):
                self._called += 1
                return 42

        my_object = MyClass()
        result = my_object.a_method()
        self.assertEqual(result, 42)
        self.assertEqual(my_object._called, 1)

        result = my_object.a_method()
        self.assertEqual(result, 42)
        self.assertEqual(my_object._called, 1)


if __name__ == '__main__':
    unittest.main()
