from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [0,0]
        for i in range(len(nums)-1):
            for j in range(len(nums)-1-i):
                if nums[i] + nums[i+j+1] == target:
                    result[0] = i
                    result[1] = i + j + 1
                    return result
    
nums = [1,2,3,4,5,6]
a = Solution()
print(a.twoSum(nums,7))

            