class Array:
    def __init__(self, size=10, type="int"):
        if type not in ['int', 'float', 'char', 'string', 'bool']:
            raise TypeError ("Can only accept int, float, char, bool or string")
        
        self._type = type
        if type == 'int':
            self._data = [0] * size

        if type == 'float':
            self._data = [0.0] * size

        if type == 'char':
            self._data = [' '] * size

        if type == 'string':
            self._data = [""] * size

        if type == 'bool':
            self._data = [True] * size

    def __getitem__(self, key):
        if key < 0 or key >= len(self._data):
            raise IndexError("Out of range")
        
        return self._data[key]

    def __setitem__(self, key, value):
        print(self._type)
        if key < 0 or key >= len(self._data):
            raise IndexError("Out of range")
        
        elif isinstance(value, int) and self._type == 'int':
            self._data[key] = value
    
        elif isinstance(value, float) and self._type == 'float':
            self._data[key] = value
    
        elif isinstance(value, bool) and self._type == 'bool':
            self._data[key] = value
    
        elif isinstance(value, str) and self._type == 'string':
            self._data[key] = value
    
        elif isinstance(value, str) and self._type == 'char':
            if len(value) == 1:
                self._data[key] = value
            else:
                raise TypeError("Char must be length 1")
        
        else:
            raise TypeError("Invalid input type. This Array only accepts " + self._type)
    
    def __str__(self):
        return str(self._data)

    def __len__(self):
        return len(self._data)

arr = Array(10)