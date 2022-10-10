from typing import List

class SumBinaryPackage:
    answer: List[str]
    _carry_flag: int
    longer_string: str
    shorter_string: str

    def __init__(self, a: str, b: str):
        if len(a) > len(b):
            self.longer_string = a
            self.shorter_string = b
        else:
            self.longer_string = b
            self.shorter_string = a

        self._carry_flag = 0
        self.answer = []

    def set_carry(self):
        self._carry_flag = 1

    def unset_carry(self):
        self._carry_flag = 0

    def get_carry_flag(self):
        return self._carry_flag

    def append_to_answer(self, num):
        if (num > 1):
            self.answer.append(str(-2 + num))
            self._carry_flag = 1
        else:
            self.answer.append(str(num))
            self._carry_flag = 0


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_package = SumBinaryPackage(a, b)


        for i in range(-1, self.negate(1 + len(sum_package.longer_string)), -1):
            self.sum_digits_and_return_carry_flag(sum_package, i)

        if sum_package.get_carry_flag()== 1:
            sum_package.answer.append("1")

        return "".join(sum_package.answer[::-1])

    def sum_digits_and_return_carry_flag(self, sum_package: SumBinaryPackage, i: int):
        shorter_digit = int(self.get_digit_or_return_zero_if_out_of_bounds(sum_package.shorter_string, i))
        sum = int(sum_package.longer_string[i]) + shorter_digit + sum_package.get_carry_flag()

        return sum_package.append_to_answer(sum)


    def negate(self, num: int) -> int:
        return num * -1

    def get_digit_or_return_zero_if_out_of_bounds(self, arr: str, index: int) -> str:
        return arr[index] if index > self.negate(len(arr) + 1) else "0"




