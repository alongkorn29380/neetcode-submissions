class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = [] # สร้าง array ปล่าว
        for x, y in points: # วนหาค่า x และ y ใน pointes
            dist = -(x ** 2 + y ** 2) # คำนวนระยะห่างระหว่าง จุด 2 จุด
            heapq.heappush(maxHeap, [dist, x, y]) # ใส่ค่ากลับไปที่ maxHeap ที่มีค่าระยะห่าง, ค่า x, ค่า y
            if len(maxHeap) > k: # นับจำนวน ถ้ามีจำนวนมากกว่า k
                heapq.heappop(maxHeap) # ให้เอาแค่ที่เกินนั้นออกไป

        res = [] # สร้าง array ปล่าว
        while maxHeap: # วน loop ใน max
            dist, x, y = heapq.heappop(maxHeap) # ถ้าเจอค่า dist, x, y  ให้เอาค่าออกจาก maxHeap
            res.append([x, y]) # ส่งค่าแค่ x, y ใน res
        return res # คืนค่า res