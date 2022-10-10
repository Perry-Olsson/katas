import pytest
from main import Solution

solution = Solution()

@pytest.mark.parametrize("binary_string1,binary_string2,expected", [
    ("0", "0", "0"),
    ("110010100101001010100101","10010010010010100101111101001001","10010011000101001011000111101110"),
    ("0","1","1"),
    ("1","1","10"),
    ("1010","101","1111"),
    ("101","101","1010")
    ])
def test_it_adds_binary_numbers_correctly(binary_string1, binary_string2, expected):
    actual = solution.addBinary(binary_string1, binary_string2)
    assert expected == actual
