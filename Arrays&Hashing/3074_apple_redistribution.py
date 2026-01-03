"""
    We use greedy algorithm to solve this problem. First we sort the capacity array in descending order.
    Then we iterate through the capacity array and add the number of capacity to the total capacity.
    If the total capacity is greater than or equal to the total apples, we return the count.
    If not, we continue to the next capacity.
"""


class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        total_apples = 0
        total_capacity = 0
        res = 0
        count = 0
        capacity.sort(reverse=True)
        for i in apple:
            total_apples = total_apples + i
        for m in capacity:
            total_capacity = total_capacity + m
            count = count + 1
            if total_capacity >= total_apples:
                res = count
                break

        return res

        