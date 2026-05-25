class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = []
        c = m = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                c += 1
            else:
                count.append(c)
                c = 0
        count.append(c)
        return max(count)