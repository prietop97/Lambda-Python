class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

map_file = "testing.txt"
paths = open(map_file, "r")

content = paths.read()
content_list = list(content.split())

print(content_list)


map_file2 = "testing2.txt"
paths2 = open(map_file2, "r")

content2 = paths2.read()
content_list2 = list(content2.split())

print(len(content_list))
print(len(content_list2))