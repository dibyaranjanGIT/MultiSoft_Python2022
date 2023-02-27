# What is a fixture in python ?
"""
In the Pytest testing framework for Python, a fixture is a function that provides a fixed set of test data or state to
be used by one or more tests. Fixtures are used to set up the environment needed for testing, such as creating database
connections or setting up test files, and they can also be used to tear down the environment after the test has been run.

To define a fixture in Pytest, you use the @pytest.fixture decorator before a function. Here's an example of a simple
fixture that provides a list of integers:
"""

import pytest

@pytest.fixture
def my_fixture():
    return [1, 2, 3, 4]

'''
This fixture function returns a list of integers, which can be used by other test functions that need it. 
To use the fixture in a test function, you simply add an argument with the same name as the fixture function:
'''


def test_my_function(my_fixture):
    assert sum(my_fixture) == 10


"""
In this example, the test_my_function function takes my_fixture as an argument and uses it to test that the sum of 
the list is equal to 10. Pytest will automatically run the fixture function before the test function to provide the 
data needed for testing.

Fixtures can be more complex than this simple example, and can include things like setting up database connections, 
creating temporary files or directories, or mocking external APIs or services. Pytest fixtures provide a powerful way 
to manage test data and dependencies in your Python tests.
"""