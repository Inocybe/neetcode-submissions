class TimeMap:
    def __init__(self):
        self.data: Dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        int_hash = hash(key)
        temp = [timestamp, value]
        if int_hash not in self.data:
            self.data[int_hash] = []
        self.data[int_hash].append(temp.copy())

    def get(self, key: str, timestamp: int) -> str:
        int_hash = hash(key)
        val1 = self.data.get(int_hash, [])
        if val1 == None: return ""

        l,r=0,len(val1)-1
        res = ""
        while l<=r:
            m=(l+r) // 2
            if val1[m][0] <= timestamp:
                res=val1[m][1]
                l=m+1
            else:
                r=m-1
        return res
        