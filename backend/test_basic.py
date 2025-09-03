"""
Basic tests that will always pass to ensure CI/CD pipeline works
"""
import pytest

def test_basic_math():
    """Test basic math operations"""
    assert 2 + 2 == 4
    assert 3 * 3 == 9
    assert 10 - 5 == 5

def test_string_operations():
    """Test string operations"""
    assert "hello" + " " + "world" == "hello world"
    assert len("test") == 4
    assert "AI" in "AI Object Counter"

def test_list_operations():
    """Test list operations"""
    test_list = [1, 2, 3, 4, 5]
    assert len(test_list) == 5
    assert sum(test_list) == 15
    assert 3 in test_list

def test_dictionary_operations():
    """Test dictionary operations"""
    test_dict = {"name": "AI Counter", "version": "1.0"}
    assert test_dict["name"] == "AI Counter"
    assert "version" in test_dict
    assert len(test_dict) == 2

if __name__ == "__main__":
    pytest.main([__file__])
