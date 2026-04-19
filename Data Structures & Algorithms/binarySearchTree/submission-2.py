class TreeMap:

    def __init__(self):
        self.treeMap = {}


    def insert(self, key: int, val: int) -> None:
        self.treeMap[key] = val

    def get(self, key: int) -> int: 
        return self.treeMap.get(key, -1)

    def getMin(self) -> int:
        if not self.treeMap:
            return -1
        min_key = min(self.treeMap.keys())
        return self.treeMap[min_key]

    def getMax(self) -> int:
        if not self.treeMap:
            return -1
        max_key = max(self.treeMap.keys())
        return self.treeMap[max_key]

    def remove(self, key: int) -> None:
        if key in self.treeMap:
            del self.treeMap[key]

    def getInorderKeys(self) -> List[int]:
        return sorted(self.treeMap.keys())
