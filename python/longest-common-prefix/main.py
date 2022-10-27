from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self._better_impl(strs)

    def _impl(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        i = 0
        while True:
            for k in range(1, len(strs)):
                str_len = len(strs[k])
                if str_len == 0:
                    return ""
                if i >= str_len:
                    return strs[k][:i]
                char = strs[k - 1][i]
                if strs[k][i] != char:
                    return strs[k][:i]
            i += 1
            


    def _better_impl(self, strs: List[str]) -> str:
        index = 0
        for char in strs[0]:
            for str in strs:
                if index >= len(str):
                    return strs[0][:index]
                if str[index] != char:
                    return strs[0][:index]
            index += 1


        return strs[0]


                
