class Node:
    def __init__(self, value):
        self.__prev = self
        self.__next = self
        self.__val = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, value):
        self.__val = value


class DoubleyLinkedList:
    def __init__(self):
        self.__dummy_node = Node(None)

    def insert(self, value):
        '''
        リストの先頭に要素を挿入
        '''
        node = Node(value)
        first_tmp = self.__dummy_node.next
        self.__dummy_node.next = node
        first_tmp.prev = node
        node.prev = self.__dummy_node
        node.next = first_tmp

    def delete(self, value):
        """
        valueをもつ最初の要素をリストから削除
        """
        node_del = self.__dummy_node.next
        while node_del != self.__dummy_node:
            if node_del.val == value:
                node_del.prev.next = node_del.next
                node_del.next.prev = node_del.prev
                del node_del
                break
            node_del = node_del.next

    def delete_first(self):
        """
        先頭の要素を削除
        """
        node_del = self.__dummy_node.next
        if node_del == self.__dummy_node:
            return
        self.__dummy_node.next = node_del.next
        node_del.next.prev = self.__dummy_node
        # del node_del

    def delete_last(self):
        """
        末尾の要素を削除
        """
        node_del = self.__dummy_node.prev
        if node_del == self.__dummy_node:
            return
        self.__dummy_node.prev = node_del.prev
        node_del.prev.next = self.__dummy_node

    def nodes(self):
        node = self.__dummy_node.next
        while node != self.__dummy_node:
            yield node
            node = node.next


def create_link():
    link = DoubleyLinkedList()
    n = int(input())
    for i in range(0, n):
        input_str = input().split()
        if input_str[0].find("i") != -1:
            link.insert(int(input_str[1]))
        elif input_str[0].find("F") != -1:
            link.delete_first()
        elif input_str[0].find("L") != -1:
            link.delete_last()
        else:
            link.delete(int(input_str[1]))
    return link

def read_lines(text):
    with open(text) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]
    return lines

def create_link_from_text(text):
    link = DoubleyLinkedList()
    lines = read_lines(text)
    n = lines[0]
    lines.pop(0)
    for val in lines:
        input_str = val.split()
        top = input_str[0]
        if top == "insert":
            link.insert(int(input_str[1]))
        elif top == "delete":
            link.delete(int(input_str[1]))
        elif top == "deleteFirst":
            link.delete_first()
        elif top == "deleteLast":
            link.delete_last()
    return link


if __name__ == "__main__":
    # link = create_link()
    link = create_link_from_text("/Users/TN27/Downloads/ALDS1_3_C-in9.txt")
    result = []
    for n in link.nodes():
        result.append(n.val)

    for i, val in enumerate(result):
        if i != len(result) - 1:
            print(val, end=" ")
        else:
            print(val)
