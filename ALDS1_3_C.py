class Node:
    def __init__(self, value, p, n):
        self.prev = p
        self.next = n
        self.val = value

class DoubleyLinkedList:
    def __init__(self):
        self.__dummy_node = Node(None, None, None)
        self.__dummy_node.next = self.__dummy_node
        self.__dummy_node.prev = self.__dummy_node

    def insert(self, value):
        node = Node(value, self.__dummy_node, self.__dummy_node.next)
        self.__dummy_node.next = node
        node.next.prev = node


    def delete(self, value):
        node_del = self.__dummy_node.next
        while node_del != self.__dummy_node:
            if node_del.val == value:
                node_del.prev.next = node_del.next
                node_del.next.prev = node_del.prev
                break
            node_del = node_del.next

    def delete_first(self):
        node_del = self.__dummy_node.next
        if node_del == self.__dummy_node:
            return
        self.__dummy_node.next = node_del.next
        node_del.next.prev = self.__dummy_node

    def delete_last(self):
        node_del = self.__dummy_node.prev
        if node_del == self.__dummy_node:
            return
        self.__dummy_node.prev = node_del.prev
        node_del.prev.next = self.__dummy_node

    def show_keys(self):
        cur_node = self.__dummy_node.next
        keys = []
        while cur_node != self.__dummy_node:
            keys.append(str(cur_node.val))
            cur_node = cur_node.next
        print(' '.join(keys))



def read_lines(text):
    with open(text) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]
    return lines


link = DoubleyLinkedList()

import sys

for i in sys.stdin:
    if 'insert' in i:
        x = i[7:-1]
        link.insert(int(x))
    elif 'deleteFirst' in i:
        link.delete_first()
    elif 'deleteLast' in i:
        link.delete_last()
    elif 'delete' in i:
        x = i[7:-1]
        link.delete(int(x))
    else:
        pass

link.show_keys()
