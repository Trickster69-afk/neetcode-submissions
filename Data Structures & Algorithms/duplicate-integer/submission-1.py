#no sorting
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = []
        l = len(nums)
        for i in nums:
            if i not in temp:
                temp.append(i)
        if l == len(temp):
            return False
        return True
