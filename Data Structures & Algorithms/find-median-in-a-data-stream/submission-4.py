class MedianFinder:

    def __init__(self):
        self.small = [] # array สำหรับเก็บค่าที่น้อย
        self.larg = [] # array เก็บค่าที่มาก

    def addNum(self, num: int) -> None:
        if self.larg and num > self.larg[0]: # ถ้า num > array ให้ใส่ลงไปมนตำแหน่งแรก
            heapq.heappush(self.larg, num)
        else:
            heapq.heappush(self.small, -1 * num) # ถ้าน้อยกว่าให้ใส่ลงไปใน array ของ small แล้ว * -1 เพื่อต้องการให้ค่าที่น้อยที่สุด

        if len(self.small) > len(self.larg) + 1: # ถ้า จำนวนของ small มากกว่า ให้ * -1 เพื่อคืนค่าให้กลายเป็น + แล้วไปใส่ที่ larg
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.larg, val)
        if len(self.larg) > len(self.small) + 1: # เหมือนกันแค่ย้ายจาก larg ที่มากกว่าไปเก็บที่ small
            val = heapq.heappop(self.larg)
            heapq.heappush(self.small,-1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.larg): #ถ้าจำนวนของ small มากกว่า ให้คืนค่าตำแหน่งแรกแล้ว * -1 เพื่อให้ค่าเป็น +
            return -1 * self.small[0]
        elif len(self.larg) > len(self.small): # ถ้า larg มากกว่าให้คืนค่าออกมา
            return self.larg[0]
        return (-1 * self.small[0] + self.larg[0]) / 2.0 # ถ้าเท่ากัน ให้เอา small ที่มีค่ามากสุดและ larg ที่มีค่าน้อยสุดมา + แล้ว / 2
        