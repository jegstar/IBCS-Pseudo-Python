class Collection:
    def __init__(self):
        self._data = []
        self._pointer = 0

    def isEmpty(self):
        return len(self._data) == 0

    def addItem(self, value):
        self._data.append(value)

    def resetNext(self):
        self._pointer = 0

    def hasNext(self):
        return self._pointer < len(self._data)

    def getNext(self):
        self._pointer += 1
        return self._data[self._pointer-1]

    def __str__(self):
        return str(self._data)

