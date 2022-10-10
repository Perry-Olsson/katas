from typing import List


class Solution: 
    def plusOne(self, digits: List[int]) -> List[int]:
        self.recurse_through_consecutive_nines(digits, len(digits) - 1)
        return digits

    def recurse_through_consecutive_nines(self, digits: List[int], index: int):
        if self.digit_is_not_nine(digits, index):
            digits[index] += 1
            return 

        digits[index] = 0

        if self.is_most_significant_digit(index):
            return self.prepend_one_to_digits(digits)

        self.recurse_through_consecutive_nines(digits, index - 1)


    def digit_is_not_nine(self, digits: List[int], index: int) -> bool:
        return digits[index] != 9

    def is_most_significant_digit(self, index: int) -> bool:
        return index == 0

    def prepend_one_to_digits(self, digits) -> None:
        digits.insert(0, 1)

