class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __iter__(self):
        # TODO: Call the constructor with the arguments you need.
        return LinkedListIterator()

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.first is None

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
        self.size += 1

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
        self.size += 1

class LinkedListIterator:
    def __init__(self):
        # TODO: set up the initial state (fields). 
        # You will need to add parameters to this constructor.

    def __next__(self):
        # TODO: return the next item and update the state, 
        # or raise `StopIteration` if there are no items left.
        return None

    def __iter__(self):
        return self

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

if __name__ == "__main__":
    custom_list = LinkedList()
    custom_list.add_first(5)
    custom_list.add_first(6)
    custom_list.add_first(7)
    custom_list.add_first(8)
    custom_list.add_last(4)

    print('the final length is', len(custom_list))

    for item in custom_list:
        print(item)
