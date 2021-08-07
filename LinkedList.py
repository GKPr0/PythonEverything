
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return "->".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __getitem__(self, index):
        return self.get(index)

    def push_front(self, node):
        node.next = self.head
        self.head = node

    def push_back(self, node):
        if self.head is None:
            self.head = node
            return

        for current_node in self:
            pass
        current_node.next = node

    def push_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            return self.push_front(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data {} not found".format(target_node_data))

    def push_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('List is empty')

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data {} not found".format(target_node_data))

    def remove(self, target_node_data):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node

        raise Exception("Node with data {} not found".format(target_node_data))

    def get(self, index):
        if self.head is None:
            raise Exception('List is empty')

        for i, node in enumerate(self):
            if i == index:
                return node

        raise Exception('List do not contain enough elements')

    def reverse(self):
        if self.head is None:
            raise Exception('Cannot reverse empty list')

        new_linked_list = LinkedList()
        for node in self:
            new_linked_list.push_front(Node(node.data))

        return new_linked_list



if __name__ == "__main__":
    llist = LinkedList(['a', 'b', 'c'])
    print(llist)

    llist.push_front(Node('f'))
    llist.push_back(Node('K'))
    print(llist)

    llist.push_before('K', Node('X'))
    llist.push_after('X', Node('!'))
    print(llist)

    llist.remove('!')
    llist.remove('f')
    print(llist)

    my_node = llist[2]
    print(my_node)

    reversed_llist = llist.reverse()
    print(reversed_llist)
