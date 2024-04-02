import pytest
from main import Solution

solution = Solution()

@pytest.mark.parametrize(
        "input,expected",
        [
            ("hello", 5),
            ("hi", 2),
            ("hows it going there buddy", 5),
            ("howdy hootin  ", 6),
            (" asdf ihdsa ydfsaf ad oha fh   d    ", 1)
        ]
        )
def test_should_return_length_of_last_word(input: str, expected: int):
    actual = solution.find_length_of_last_word(input)
    assert expected == actual

