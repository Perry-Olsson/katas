import pytest
from main import Solution

solution = Solution()

@pytest.mark.parametrize("input,expected", [
    ([0],[1]),
    ([1], [2]),
    ([5], [6]),
    ([9], [1, 0])
    ])
def test_it_adds_one_to_single_digit_number(input, expected):
    actual = solution.plusOne(input)
    assert expected == actual

@pytest.mark.parametrize("input,expected", [
    ([1, 0], [1, 1]),
    ([2, 5], [2, 6]),
    ([2, 9], [3, 0]),
    ([9, 9], [1, 0, 0])
    ])
def test_it_adds_one_to_double_digit_number(input, expected):
    actual = solution.plusOne(input)
    assert expected == actual

@pytest.mark.parametrize("input,expected", [
    ([1, 0, 0], [1, 0, 1]),
    ([1, 0, 9], [1, 1, 0]),
    ([1, 9, 9], [2, 0, 0]),
    ([9, 9, 9], [1, 0, 0, 0]),
    ])
def test_it_adds_one_to_triple_digit_number(input, expected):
    actual = solution.plusOne(input)
    assert expected == actual

@pytest.mark.parametrize("input,expected", [
    ([1, 0, 0, 9, 9, 9, 9, 9, 9], [1, 0, 1, 0, 0, 0, 0, 0, 0]),
    ([9, 9, 9, 9, 9, 9, 9, 9, 9], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ])
def test_it_adds_one_to_large_number(input, expected):
    actual = solution.plusOne(input)
    assert expected == actual
