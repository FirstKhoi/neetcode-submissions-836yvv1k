class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
        self.size = 0

    
    def get(self, index: int) -> int:
        if 0 <= index < self.size:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
            return curr.val
        else:
            return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node
        self.size += 1 

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1 

    def remove(self, index: int) -> bool:
        if 0 <= index < self.size:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            self.size -= 1
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        result = []
        curr = self.head.next
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result
