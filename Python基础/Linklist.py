class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def output_list(self):
        current_node = self.head
        while current_node:
            if current_node.next:
                print(current_node.data, end="-->")
            else:
                print(current_node.data)
            current_node = current_node.next


def main():
    linked_list = LinkedList()
    
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    linked_list.output_list()

if __name__ == "__main__":
    main()