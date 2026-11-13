class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        res, prve = 1, ""

        while r < len(arr):
            if arr[r - 1] > arr[r] and prve != ">":
                res = max(res, r - l + 1)
                r += 1
                prve = ">"
            elif arr[r - 1] < arr[r] and prve != "<":
                res = max(res, r - l + 1)
                r += 1
                prve = "<"
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prve = ""
        return res