class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        
        return None

    def pop(self):
        if len(self.items) == 0:
            return None

        removed_item = self.items[-1]
        del self.items[-1]
        
        return removed_item
        
