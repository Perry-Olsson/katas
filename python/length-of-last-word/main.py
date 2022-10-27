class Solution:
    def find_length_of_last_word(self, input: str) -> int:
        return self._find_length_of_last_word_functional(input)

    def _find_length_of_last_word(self, input: str) -> int:
        length_of_last_word = 0
        found_first_character = False
        for i in range(len(input) - 1, -1, -1):
            if input[i] == " ":
                if found_first_character is True:
                    break
            else:
                found_first_character = True
                length_of_last_word += 1

        return length_of_last_word

    def _find_length_of_last_word_alternate(self, input: str) -> int:
        index_of_last_char = self._find_index_of_last_char(input)
        return self._count_length_of_word_reverse(input, index_of_last_char)


    def _find_index_of_last_char(self, input: str) -> int:
        for i in range(len(input) - 1, -1, -1):
            if input[i] != " ":
                return i

        return 0

    def _count_length_of_word_reverse(self, str: str, index_of_last_char: int) -> int:
        index = index_of_last_char
        while index > -1:
            if str[index] == " ":
                break
            index -= 1

        return index_of_last_char - index

    def _find_length_of_last_word_functional(self, input: str) -> int:
        return len(input.strip().split()[-1])
