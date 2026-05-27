class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        c = -1
        for i in range(l-1, -1, -1):
            c, arr[i] = max(arr[i], c), c
        return arr
        