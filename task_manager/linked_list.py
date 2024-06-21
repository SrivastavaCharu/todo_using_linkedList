class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = Node(task)
        new_node.next = self.head
        self.head = new_node

    def view_task(self):
        current = self.head
        tasks = []
        while current:
            tasks.append(current.data)
            current = current.next
        return tasks
    
    def complete_task(self, task):
        current = self.head
        prev = None
        while current and current.data != task:
            prev = current
            current = current.next
        if current:
            if prev: 
                prev.next = current.next
            else:
                self.head = current.next
            return True
        return False
