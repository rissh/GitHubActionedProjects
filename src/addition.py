# app.py
"""
This module contains a simple function for addition and corresponding tests.
"""

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def test_add():
    """Test cases for the add function."""
    assert add(1, 2) == 3, "1 + 2 should equal 3"
    assert add(1, -1) == 0, "1 + (-1) should equal 0"
    assert add(0, 0) == 0, "0 + 0 should equal 0"
    assert add(-1, -1) == -2, "(-1) + (-1) should equal -2"

if __name__ == "__main__":
    test_add()
    print("All tests passed!")

