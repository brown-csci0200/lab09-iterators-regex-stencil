class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.size = 0
        self.first = None
        self.last = None

    def __iter__(self):
        # TODO:
        # 1. create a field in the class indicating which element to start iterating from, e.g. self.current = ...
        # 2. return self
        pass

    def __next__(self):
        # TODO: write the next method for a LinkedList!
        pass

    def is_empty(self):
        return self.first is None and self.last is None

    def add_first(self, value):
        if self.is_empty():
            new_node = Node(value)
            self.first = new_node
            self.last = new_node
        else:
            new_node = Node(value)
            new_node.next = self.first
            self.first.prev = new_node
            self.first = new_node

    def add_last(self, value):
        if self.is_empty():
            new_node = Node(value)
            self.first = new_node
            self.last = new_node
        else:
            new_node = Node(value)
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node


if __name__ == "__main__":
    my_list = LinkedList()
    my_list.add_first(5)
    my_list.add_first(6)
    my_list.add_first(7)
    my_list.add_first(8)
    my_list.add_last(4)

    # when your iter and next methods work, this for loop
    # should print the elements of  my_list!
    for node in my_list:
        print(node.value)
