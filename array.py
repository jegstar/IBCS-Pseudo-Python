class Array:
    def __init__(self, size):
        self._data = [0] * size

    def __getitem__(self, key):
        if key < 0 or key >= len(self._data):
            raise IndexError("Out of range")
        else:
            return self._data[key]

    def __setitem__(self, key, value):
        if key < 0 or key >= len(self._data):
            raise IndexError("Out of range")
        else:
            self._data[key] = value
    
    def __str__(self):
        return str(self._data)

    def __len__(self):
        return len(self._data)
