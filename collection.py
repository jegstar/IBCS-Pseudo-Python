class Collection:
    def __init__(self):
        self.data = []
        self.pointer = 0

    def isEmpty(self):
        return len(self.data) == 0

    def addItem(self, value):
        self.data.append(value)

    def resetNext(self):
        self.pointer = 0

    def hasNext(self):
        return self.pointer < len(self.data)

    def getNext(self):
        self.pointer += 1
        return self.data[self.pointer-1]

    def __str__(self):
        return str(self.data)

