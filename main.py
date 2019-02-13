class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        if self.head is None:
            return None

        node = self.head

        while node:
            if val == node.value:
                return node
            node = node.next

        return None

    def find_all(self, val):
        node = self.head
        findList = []

        if self.head is None:
            return findList

        while node:
            if node.value == val:
                findList.append(node)

            node = node.next

        return findList

    def delete(self, val, all=False):
        node = self.head

        if self.head is None:
            return None

        if node.next is None:
            self.head = None
            self.tail = self.head
            return

        while node:
            if self.head.value == val:
                self.head = node.next
                if node.next is None:
                    self.tail = self.head
                node = node.next
                if all == True:
                    continue

            if node.value == val:
                if node.next is None:
                    self.tail = node.prev
                    node.prev.next = node.next
                    return

                node.prev.next = node.next
                node.next.prev = node.prev


                if all == False:
                    return

            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        count = 0


        if node is None:
            return count

        while node:
            count = count + 1
            node = node.next

        return count

    def insert(self, afterNode, newNode):
        node = self.head

        if afterNode == None:
            if node == None:
                self.head = newNode
                self.tail = self.head

            elif node:
                self.add_in_tail(newNode)

        while node:
            if node == afterNode:
                newNode.prev = node.prev
                newNode.next = node.next
                node.next = newNode
                node.next.prev = newNode

                if newNode.next == None:
                    self.tail = newNode

            node = node.next

    def add_in_head(self, newNode):
        node = self.head
        self.head = newNode

        if node is None:
            self.tail = self.head
            return

        else:
            self.head.next = node
            node.prev = self.head

        if node.next is None:
            self.tail = node



    # def print_all_nodes(self):
    #     node = self.head
    #
    #     while node:
    #         print(node.value)
    #         node = node.next



# list = LinkedList2()
# list.add_in_tail(Node(1))
# list.add_in_tail(Node(2))
# list.add_in_tail(Node(3))
#
# list.add_in_head(Node(4))
# list.print_all_nodes()
# print("list len",list.len())
#
# # list.delete(3)
# # list.print_all_nodes()
# # list.clean()
# # print("list len",list.len())
# # list.print_all_nodes()
# #
# a = list.head
# b = list.tail
# print("list head value", a.value)
# print("list tail value", b.value)

# *****TESTS*****

def findTest():
    list = LinkedList2()
    list.add_in_tail(Node(1))

    print("First node search test")

    a = list.find(1)

    if a.value == 1:
        print("Test OK")
    else:
        print("Test ERROR")

findTest();

def findAllTest():
    list = LinkedList2()
    list.add_in_tail(Node(1))
    list.add_in_tail(Node(1))

    print("Test of searching all nodes for a specific value")

    a = list.find_all(1)
    b = [1, 1, 1]

    if a[0].value == b[0] and a[1].value == b[1]:
        print("Test OK")
    else:
        print("Test ERROR")

findAllTest()

def deleteTest1():
    print("Delete test1")
    list = LinkedList2()
    list.add_in_tail(Node(2))
    list.add_in_tail(Node(2))
    list.add_in_tail(Node(3))
    list.add_in_tail(Node(3))
    list.add_in_tail(Node(2))
    list.add_in_tail(Node(2))

    list.delete(2, True)
    a = list.find_all(2)
    if a == [] and list.head.value == 3 and list.tail.value == 3:
        print("Test OK")
    else:
        print("Test ERROR")

deleteTest1()

def deleteTest2():
    print("Delete test2")
    list = LinkedList2()
    list.add_in_tail(Node(2))
    list.add_in_tail(Node(2))
    list.add_in_tail(Node(3))
    list.add_in_tail(Node(3))
    list.add_in_tail(Node(3))
    list.add_in_tail(Node(3))

    list.delete(2, True)
    a = list.find_all(2)
    if a == [] and list.head.value == 3 and list.tail.value == 3:
        print("Test OK")
    else:
        print("Test ERROR")

deleteTest2()

def deleteTest3():
    print("Delete test3")
    list = LinkedList2()
    list.add_in_tail(Node(3))
    list.add_in_tail(Node(3))
    list.add_in_tail(Node(3))
    list.add_in_tail(Node(3))
    list.add_in_tail(Node(2))
    list.add_in_tail(Node(2))

    list.delete(2, True)
    a = list.find_all(2)
    if a == [] and list.head.value == 3 and list.tail.value == 3:
        print("Test OK")
    else:
        print("Test ERROR")

deleteTest3()

def deleteTest4():
    print("Delete test4")
    list = LinkedList2()
    list.add_in_tail(Node(3))

    list.delete(3)
    a = list.find_all(3)
    if a == [] and list.head == None and list.tail == None:
        print("Test OK")
    else:
        print("Test ERROR")

deleteTest4()

def deleteTest5():
    print("Delete test5")
    list = LinkedList2()
    list.add_in_tail(Node(3))
    list.add_in_tail(Node(2))
    list.add_in_tail(Node(2))

    list.delete(3)
    a = list.find_all(3)
    if a == [] and list.head.value == 2 and list.tail.value == 2:
        print("Test OK")
    else:
        print("Test ERROR")

deleteTest5()

def deleteTest6():
    print("Delete test6")
    list = LinkedList2()
    list.add_in_tail(Node(2))
    list.add_in_tail(Node(3))
    list.add_in_tail(Node(2))

    list.delete(3)
    a = list.find_all(3)
    if a == [] and list.head.value == 2 and list.tail.value == 2:
        print("Test OK")
    else:
        print("Test ERROR")

deleteTest6()

def deleteTest7():
    print("Delete test7")
    list = LinkedList2()
    list.add_in_tail(Node(2))
    list.add_in_tail(Node(2))
    list.add_in_tail(Node(3))

    list.delete(3)
    a = list.find_all(3)
    if a == [] and list.head.value == 2 and list.tail.value == 2:
        print("Test OK")
    else:
        print("Test ERROR")

deleteTest7()

def cleanTest():
    print("cleanTest")
    list = LinkedList2()
    list.add_in_tail(Node(3))
    list.add_in_tail(Node(3))
    list.add_in_tail(Node(3))

    a = list.clean()

    if a is None:
        print("Test OK")
    else:
        print("Test ERROR")

cleanTest()

def lenTest():
    print("lenTest")
    list = LinkedList2()
    list.add_in_tail(Node(3))
    list.add_in_tail(Node(3))
    list.add_in_tail(Node(3))

    a = list.len()

    if a == 3:
        print("Test OK")
    else:
        print("Test ERROR")

lenTest()

def insertTest1():
    print("insert Test1")
    list = LinkedList2()
    list.add_in_tail(Node(1))
    list.add_in_tail(Node(2))
    list.add_in_tail(Node(3))

    list.insert(list.find(2), Node(4))
    a = list.find(4)

    if a.value == 4 and list.head.value == 1 and list.tail.value == 3:
        print("Test OK")
    else:
        print("Test ERROR")

insertTest1()

def insertTest2():
    print("insert Test2")
    list = LinkedList2()
    list.add_in_tail(Node(1))
    list.add_in_tail(Node(2))
    list.add_in_tail(Node(3))

    list.insert(list.find(3), Node(4))
    a = list.find(4)

    if a.value == 4 and list.head.value == 1 and list.tail.value == 4:
        print("Test OK")
    else:
        print("Test ERROR")

insertTest2()

def insertTest3():
    print("insert Test3")
    list = LinkedList2()
    list.add_in_tail(Node(1))
    list.add_in_tail(Node(2))
    list.add_in_tail(Node(3))

    list.insert(list.find(5), Node(4))
    a = list.find(4)

    if a.value == 4 and list.head.value == 1 and list.tail.value == 4:
        print("Test OK")
    else:
        print("Test ERROR")

insertTest3()

def insertTest4():
    print("insert Test4")
    list = LinkedList2()

    list.insert(list.find(5), Node(4))
    a = list.find(4)

    if a.value == 4 and list.head.value == 4 and list.tail.value == 4:
        print("Test OK")
    else:
        print("Test ERROR")

insertTest4()

def addInHeadTest1():
    print("Add in head test1")
    list = LinkedList2()
    list.add_in_tail(Node(1))
    list.add_in_head(Node(4))

    if list.head.value == 4 and list.tail.value == 1:
        print("Test OK")
    else:
        print("Test ERROR")

addInHeadTest1()

def addInHeadTest2():
    print("Add in head test2")
    list = LinkedList2()
    list.add_in_head(Node(4))

    if list.head.value == 4 and list.tail.value == 4:
        print("Test OK")
    else:
        print("Test ERROR")

addInHeadTest2()