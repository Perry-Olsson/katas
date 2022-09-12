from main import Solution 

solution = Solution()
def test_it_returns_fizzbuzz_if_divisible_by_3_and_5():
    val = solution.fizz_buzz(15)
    assert val[14] == "FizzBuzz"

def test_it_returns_fizz_if_divisible_by_3():
    val = solution.fizz_buzz(6)
    assert val[5] == "Fizz"

def test_it_returns_buzz_if_divisible_by_5():
    val = solution.fizz_buzz(5)
    assert val[4] == "Buzz"

def test_it_returns_num_if_not_divisible_by_3_or_5():
    val = solution.fizz_buzz(8)
    assert val[7] == "8"

def test_returns_correct_amount_of_nums():
    num = 102
    val = solution.fizz_buzz(num)
    assert len(val) == num

def test_array_is_one_indexed():
    num = 3
    fizz_buzz_arr = solution.fizz_buzz(num)
    assert fizz_buzz_arr[0] == "1"

