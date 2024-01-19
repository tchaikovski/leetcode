from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, num in enumerate(nums):
            search_num = target - num
            if search_num in num_dict:
                return [num_dict[search_num], i]
            num_dict[num] = i

        return []