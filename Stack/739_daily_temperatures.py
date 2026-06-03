"""
    We use a stack to solve this problem. We iterate through the temperatures and add the temperature and its index to the stack.
    If the temperature is greater than the top of the stack, we pop the top of the stack and calculate the difference between the current index and the index of the top of the stack.
    We then update the result list with the difference.
    If the temperature is not greater than the top of the stack, we add the temperature and its index to the stack.
    If we finish the loop, we return the result list.
"""


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j

            stack.append(i)

        return ans



        