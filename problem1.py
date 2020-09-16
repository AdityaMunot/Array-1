# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Three line explanation of solution in plain english
""" Generated product while moving to right """
# Your code here along with comments explaining your approach

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums or len(nums)==0: return [0]

        result = [0]*len(nums)
        prod = 1
        for x in range(len(nums)):
            result[x] = prod
            prod = prod * nums[x]

        prod=1
        for x in range(len(nums)-1, -1, -1):
            result[x] = result[x] * prod
            prod = prod * nums[x]

        return result