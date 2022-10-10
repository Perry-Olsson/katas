from typing import List


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer: List[str] = []
        carry_flag: int = 0
        
        if len(a) > len(b):
            longer_string = a
            shorter_string = b
        else:
            longer_string = b
            shorter_string = a

        longer_arr = list(longer_string)
        shorter_arr = list(shorter_string)
        length_difference = len(longer_arr) - len(shorter_arr)

        for i in range(len(longer_arr) - len(shorter_arr)):
            shorter_arr.insert(0, "0")

        for i in reversed(range(len(longer_string))):
            shorter_digit = int(shorter_arr[i]) if i < len(shorter_arr) else 0
            sum_of_digits = int(longer_arr[i]) + shorter_digit + carry_flag
            if (sum_of_digits > 1):
                answer.append(str(-2 + sum_of_digits))
                carry_flag = 1
            else:
                answer.append(str(sum_of_digits))
                carry_flag = 0

        if carry_flag == 1:
            answer.append("1")

        return "".join(answer[::-1])


