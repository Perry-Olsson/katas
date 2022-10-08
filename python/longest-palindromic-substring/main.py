class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self._fastest_solution(s)

    def _fastest_solution(self, s: str) -> str:
        longest_tuple = (0, 0)
        for i in range(len(s)):
            odd = self._longest_palindrome_odd(s, i)
            even = self._longest_palindrome_even(s, i)
            odd_len = odd[1] - odd[0]
            even_len = even[1] - even[0]
            tuple = (odd[0], odd[1]) if odd_len > even_len else (even[0], even[1])
            if tuple[1] - tuple[0] > longest_tuple[1] - longest_tuple[0]:
                longest_tuple = tuple

        return s[longest_tuple[0]:longest_tuple[1] + 1]

    def _longest_palindrome_odd(self, s: str, index: int) -> tuple:
        if index == 0 or index == len(s) - 1:
            return (0, 0)
        left = index - 1
        right = index + 1
        return self._longest_palindrome(s, left, right)

    def _longest_palindrome_even(self, s: str, index: int) -> tuple:
        if index == len(s) - 1:
            return (0, 0)
        left = index
        right = index + 1
        return self._longest_palindrome(s, left, right)

    def _longest_palindrome(self, s: str, left: int, right: int):
        while left >= 0 and right <= len(s) - 1:
            if s[left] != s[right]:
                break
            left -= 1
            right += 1

        return (left + 1, right - 1)


    def faster_solution(self, s: str) -> str:
        if s == "":
            return s
        start = 0
        end = 1
        cur_len = 1
        str_len = len(s)
        for i in range(str_len - 1):
            for j in range(i + 1, str_len):
                potential_len = j - i + 1
                if cur_len >= potential_len:
                    continue
                if self._is_palindrome(s, i, j):
                    if potential_len > cur_len:
                        start = i
                        end = j + 1
                        cur_len = potential_len



        return s[start:end]

    def naive_solution(self, s: str) -> str:
        if s == "":
            return s
        current_longest_palindrome = s[0]
        for i in range(len(s) - 1):
            for j in range(i + 2, len(s) + 1):
                sub_str = s[i:j]
                if self._is_palindrome(sub_str):
                    if len(sub_str) > len(current_longest_palindrome):
                        current_longest_palindrome = sub_str

        return current_longest_palindrome

    def _is_palindrome_2(self, s: str) -> bool:
        return s == s[::-1]

    def _is_palindrome(self, s: str, start = 0, end = None) -> bool:
        end = len(s) - 1 if end is None else end
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

def main():
    solution = Solution()
    val = solution.longestPalindrome("heybabasdftacocatasdffdasatacocata")
    print(val)

main()

