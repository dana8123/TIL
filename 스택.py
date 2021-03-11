def push(self, value):
    new_head = Node(value)
    new_head.next = self.head
    self.head = new_head


def pop(self):
    if self.is_empty():
        return "stack is empty"
    delete_head = self.head
    self.head = self.head.next
    return delete_head


def peek(self):
    if self.is_empty():
        return "stack is empty"

    return self.head.data


def is_empty(self):
    return self.head is
