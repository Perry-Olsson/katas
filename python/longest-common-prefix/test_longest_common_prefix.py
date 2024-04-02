from typing import List
import pytest
from main import Solution

s = Solution()

@pytest.mark.parametrize(
        "input,expected",
        [
            (["", "b"], ""),
            (["b", ""], ""),
            ([""], ""),
            (["fs", "ab", "cd"], ""),
            (["flower","flower","flower","flower"], "flower"),
            (["flow", "flower", "flight"], "fl"),
            (["flow", "f", "fb"], "f"),
            (["flow", "floaflalowa", "floaflalowafla"], "flo")
        ]
        )
def test_should_return_longest_common_prefix(input: List[str], expected: str):
    actual = s.longestCommonPrefix(input)
    assert expected == actual


