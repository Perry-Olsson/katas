from typing import List


class Solution: 
    def plus_one(self, digits: List[int]) -> List[int]:
        self.handle_nines(digits, len(digits) - 1)
        return digits

    def handle_nines(self, digits: List[int], index: int):
        if digits[index] != 9:
            digits[index] += 1
            return

        digits[index] = 0

        if index == 0:
            digits.insert(0, 1)
            return 

        self.handle_nines(digits, index - 1)

