class Stack:

    def __init__(self, items = [], limit = 100):
       self.items = items
       self.limit = limit

    def isEmpty(self):
        if len(self.items)== 0:
            return True
        else:
            return False

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
            return self.items
        else:
            return 'Stack Overflow'

    def pop(self):
        if len(self.items) > 0:
          return self.items.pop()
        else:
            return IndexError('Pop from empty stack')

    def peek(self):
        if len(self.items) > 0:
           return self.items[-1]
        else:
            return None
    
    def size(self):
        if len(self.items) > 0:
         return len(self.items)

    def full(self):
        if len(self.item) > 0:
            return 'Full'

    def search(self, target):
        for index, item in enumerate(reversed(self.items)):
            if item == target:
                return index
           
        return -1
    def full(self):
      return len(self.items) >= self.limit

    # def empty(self):
    #     if len(self.items) == 0:
    #         return True
    #     else: 
    #         return False
    def empty(self):
        if len(self.items) == 0:
            return 1 
        else:
            return 0  
