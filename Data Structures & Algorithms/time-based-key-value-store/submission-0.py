class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        arr = self.keyStore.get(key, [])
        arr.append([timestamp, value])
        self.keyStore[key] = arr

    def get(self, key: str, timestamp: int) -> str:
        arr = self.keyStore.get(key, [])
        l, r = 0, len(arr) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2
            if arr[m][0] <= timestamp:
                res = arr[m][1]
                l = m + 1
            else:
                r = m - 1
        return res