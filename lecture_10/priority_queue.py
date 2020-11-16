class Queue:
    def __init__(self):
        self.lst = []

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        if self.is_empty():
            return 'Error'
        return self.lst.pop(0)

    def is_empty(self):
        return len(self.lst) == 0

    def top(self):
        if self.is_empty():
            return 'Error'
        return self.lst[0]


def get_key(item):
    return item[0]


class PriorityQueue(Queue):
    def push(self, x):
        return 'Not relevant!'

    def priority_push(self, priority, x):
        self.lst.append((priority, x))
        self.lst.sort(key=get_key)

    def pop(self):
        if self.is_empty():
            return 'Error'
        tup = self.lst.pop(0)
        return tup[1]


pr = PriorityQueue()
pr.priority_push(5, 3)
pr.priority_push(1, 10)
pr.priority_push(2, 10)
pr.priority_push(1, 9)

print(pr.pop())
print(pr.pop())
print(pr.pop())
print(pr.pop())
