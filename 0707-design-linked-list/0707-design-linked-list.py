class ListNode:
    def __init__(self, val = None, next = None, prv = None):
        self.val = val
        self.next = next
        self.prv = prv

class MyLinkedList:

    def __init__(self):
        self.head = ListNode("head")
        self.tail = ListNode("tail")
        self.head.next, self.tail.prv = self.tail, self.head
        self.length = 0
        
    def printList(self):
        temp = self.head
        while temp:
            print(temp.val,"-->",end ="")
            temp = temp.next
        print()
        
    def get(self, index: int) -> int:
        # print("index:" ,index, "length",self.length)
        if index not in range(self.length): return -1
        idx = 0
        temp = self.head.next
        while temp and temp!= self.tail and idx != index:
            temp = temp.next
            idx += 1
        # print("get Index:", index," ",end="")
        # self.printList()
        return temp.val
        

    def addAtHead(self, val: int) -> None:
        next ,prv= self.head.next, self.head
        self.head.next = ListNode(val, next, prv)
        next.prv = self.head.next
        self.length += 1
        # print("Add Head:", val," ",end="")
        # self.printList()
         

    def addAtTail(self, val: int) -> None:
        next, prv = self.tail, self.tail.prv
        prv.next = ListNode(val,next,prv)
        next.prv = prv.next
        self.length += 1
        # print("Add Tail:", val," ",end="")
        # self.printList()

        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.length:
            return self.addAtTail(val)
        if index == 0:
            return self.addAtHead(val)
        if index not in range(self.length): return -1
        
        idx = 0
        temp = self.head.next
        while temp and idx != index:
            temp = temp.next
            idx += 1
            
        prv = temp.prv
        prv.next = ListNode(val,temp,prv)
        temp.prv = prv.next
        self.length += 1
        
        # print("Add Index:", index,"val: ",val)
        # self.printList()            
        

    def deleteAtIndex(self, index: int) -> None:
        if index not in range(self.length): return

        idx = 0
        temp = self.head.next
        while temp and temp != self.tail and idx != index:
            temp = temp.next
            idx += 1
            
        prv,next = temp.prv, temp.next
        prv.next, next.prv = next, prv
        self.length -= 1
        
        # print("Remove Index:", index," ",end="")
        # self.printList()

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)