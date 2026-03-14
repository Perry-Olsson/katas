class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        initial = [0, 1]
        for i in range(1, n):
            power = 2**i
            for i in range(len(initial) - 1, -1, -1):
                initial.append(initial[i] + power)
        return initial
