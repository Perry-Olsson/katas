from typing import List
import pytest
from main import Solution, from_list, to_list

s = Solution()



@pytest.mark.parametrize(
        "list1,list2,expected",
        [
            ([1, 4, 5], [3, 7, 10], [1, 3, 4, 5, 7, 10]),
            ([1, 2, 4, 5], [3, 7, 10], [1, 2, 3, 4, 5, 7, 10]),
            ([1, 2, 4, 5, 10, 11, 12], [1, 3, 7, 10], [1, 1, 2, 3, 4, 5, 7, 10, 10, 11, 12]),
        ]
        )
def test_should_return_longest_common_prefix(list1: List[int], list2: List[int], expected: List[int]):
    ll_head_1 = from_list(list1)
    ll_head_2 = from_list(list2)
    merged_ll = s.mergeTwoLists(ll_head_1, ll_head_2)
    actual = to_list(merged_ll)
    assert expected == actual


