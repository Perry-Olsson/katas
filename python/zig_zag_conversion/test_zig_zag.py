from solution import Solution


def test_1():
    assert "PAHNAPLSIIGYIR" == Solution().convert("PAYPALISHIRING", 3)

# P      I       N
# A    L S     I G
# Y  A   H  R
# P      I
def test_2():
    assert "PINALSIGYAHRPI" == Solution().convert("PAYPALISHIRING", 4)

def test_3():
    assert "A" == Solution().convert("A", 1)

def test_4():
    assert "A" == Solution().convert("A", 2)

def test_5():
    assert "AB" == Solution().convert("AB", 1)

def test_6():
    assert "AB" == Solution().convert("AB", 2)

def test_6():
    assert "ACBD" == Solution().convert("ABCD", 2)
