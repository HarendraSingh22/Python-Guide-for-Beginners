class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def append(self, value):
        node = Node(value)
        if(self.root == None):
            self.root = node
            return

        temp = self.root
        while(temp.next != None):
            temp = temp.next

        temp.next = node

    def addFront(self, value):
        if(self.root == None):
            return

        node = Node(value)
        temp = self.root
        node.next = temp
        self.root = node

    def delete(self, listValue):
        if(self.root == None):
            return

        temp = self.root
        while(temp.next.value != listValue and temp.next != None):
            temp = temp.next

        if(temp.value != listValue):
            return
        tempOne = temp.next
        tempTwo = temp.next.next

        tempOne.next = None
        temp.next = tempTwo

    def deleteIndex(self, index):
        if(self.root == None):
            return
        if(index > self.len()-1):
            return

        temp = self.root
        counter = 0
        while(counter != index-1):
            temp = temp.next
            counter += 1

        tempOne = temp.next
        tempTwo = temp.next.next

        tempOne.next = None
        temp.next = tempTwo

    def deleteFront(self):
        if(self.root == None):
            return

        temp = self.root
        tempOne = temp.next

        temp.next = None
        tempOne = self.root

    def deleteLast(self):
        if(self.root == None):
            return
        if(self.root.next == None):
            self.root = None
            return

        temp = self.root
        while(temp.next.next != None):
            temp = temp.next
        temp.next = None

    def addPreValue(self, listValue, insertValue):
        if(self.root == None):
            return

        node = Node(insertValue)
        temp = self.root
        while(temp.next.value != listValue):
            temp = temp.next

        tempOne = temp.next
        temp.next = node
        node.next = tempOne

    def addPostValue(self, listValue, insertValue):
        if(self.root == None):
            return

        node = Node(insertValue)
        temp = self.root
        while(temp.value != listValue):
            temp = temp.next

        tempOne = temp.next
        temp.next = node
        node.next = tempOne

    def deletePreValue(self, listValue):
        if(self.root == None):
            return

        temp = self.root
        while(temp.next.next.value != listValue):
            temp = temp.next

        tempOne = temp.next
        tempTwo = temp.next.next
        tempOne.next = None
        temp.next = tempTwo

    def deletePostValue(self, listValue):
        if(self.root == None):
            return

        tmep = self.root
        while(temp.value != listValue):
            temp = temp.next

        tempOne = temp.next
        tempTwo = temp.next.next
        tempOne.next = None
        temp.next = tempTwo

    def len(self):
        if(self.root == None):
            return 0

        temp = self.root
        counter = 0
        while(temp != None):
            counter += 1

        return counter

    def __repr__(self):
        if(self.root == None):
            return ''

        string = ''
        temp = self.root
        while(temp != None):
            string = string+f'[{temp.value}-]->'
            temp = temp.next

        return string


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(2)
    ll.addFront(1)
    ll.addPostValue(2, 3)
    print(ll)
