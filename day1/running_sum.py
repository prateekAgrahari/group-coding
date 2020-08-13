class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst = list()
        add = 0
        for i in range(len(nums)):
            add += nums[i]
            lst.append(add)
        return lst
