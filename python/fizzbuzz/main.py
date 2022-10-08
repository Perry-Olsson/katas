class Solution:
    def fizz_buzz(self, n: int):
        return [self._get_fizz_buzz_value(x) for x in range(1, n + 1)]

    def _get_fizz_buzz_value(self, num: int):
        if num == 0:
            return str(num)
        mod_3 = num % 3
        mod_5 = num % 5
        if mod_3 == 0 and mod_5 == 0:
            return "FizzBuzz"
        if mod_5 == 0:
            return "Buzz"
        if mod_3 == 0:
            return "Fizz"
        return str(num)

def main():
    solution = Solution()
    val = solution.fizz_buzz(10)
    print(val)

main()
