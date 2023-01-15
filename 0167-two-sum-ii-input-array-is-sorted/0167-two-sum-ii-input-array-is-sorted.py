class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(numbers) - 1
        while start < end:
            s = numbers[start] + numbers[end]
            if s == target: return [start + 1 , end + 1]
            elif s > target: end -= 1
            else: start += 1
        