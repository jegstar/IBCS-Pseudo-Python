class Array:
    def __init__(self, size):
        self.data = [0] * size

    def __getitem__(self, key):
        if key < 0 or key >= len(self.data):
            raise IndexError("Out of range")
        else:
            return self.data[key]

    def __setitem__(self, key, value):
        if key < 0 or key >= len(self.data):
            raise IndexError("Out of range")
        else:
            self.data[key] = value
    
    def __str__(self):
        return str(self.data)

arr = Array(5)
print(arr)
arr[5]= 3

print(arr)