from multiprocessing.dummy import current_process


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begin(self,data):
         new_node = Node(data)
         new_node.next = self.head
         self.head = new_node

    #def delete_begin(self):
        #if self.head:
            #self.head = self.head.next

    #def delete_end(self):
        #if self.head is None or self.head.next is None:
            #self.head = None
            #return

        #current = self.head
        #while current.next.next:
            #current = current.next
        #current.next = None

    def delete_middle(self,key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current:
            prev.next = current.next




    def print_list(self):
        current = self.head
        while current:
            print(current.data,end = "->")
            current = current.next
        print("None")



l = Linkedlist()
l.insert_at_begin(10)
l.insert_at_begin(15)
l.insert_at_begin(30)
l.insert_at_begin(45)
l.print_list()
l.delete_middle(15)
l.print_list()