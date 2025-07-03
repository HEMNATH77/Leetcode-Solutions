class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    #def insert_at_begin(self,data):
        # new_node = Node(data)
        # new_node.next = self.head
        # self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head  is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
           current = current.next
        current.next = new_node

    def insert_after_gn_node(self,data,previous):
        current = self.head
        while current and current.data != previous:
            current = current.next
        if not current:
            return

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data,end = "->")
            current = current.next
        print("None")
l = Linkedlist()
l.insert_at_end(10)
l.insert_at_end(15)
l.insert_at_end(30)
l.print_list()
l.insert_after_gn_node(20,15)
l.print_list()