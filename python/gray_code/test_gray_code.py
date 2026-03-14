from gray_code import Solution

def test_1():
    assert Solution().grayCode(2) == [0, 1, 3, 2]

def test_2():
    assert Solution().grayCode(1) == [0, 1]

def test_3():
    assert Solution().grayCode(3) == [0, 1, 3, 2, 6, 7, 5, 4]
