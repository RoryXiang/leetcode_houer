"""思路：
    最后一个数能跳出去，反推，倒数第二个能跳到最后一个，依次类推
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        num = len(nums)
        end = num - 1
        start = end - 1
        while start > 0:
            if nums[start] + start >= end:
                end = start
            start -= 1
        return nums[start] + start >= end
