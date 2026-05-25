class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        c = 1
        l = len(arr)
        for i in range(l):
            if c == l:
                arr[l - 1] = -1
                break
            k = max(arr[c:])
            arr[i] = k
            c += 1
        return arr
        