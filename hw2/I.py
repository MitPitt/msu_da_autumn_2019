import copy

class FragileDict:
    
    def __init__(self, data = None):
        self._lock = False
        if data == None:
            self._data = dict()
        else:
            self._data = copy.deepcopy(data)
    
    def __enter__(self):
        self._lock = True
        self._data1 = copy.deepcopy(self._data)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._lock = False
        if not exc_type:
            self._data = copy.deepcopy(self._data1)
            del self._data1
        else:
            del self._data1
            print("Exception has been suppressed.")
            return True
    
    def __setitem__(self, key, value):
        if self._lock:
            self._data1[key] = value
        else:
            raise RuntimeError("Protected state")

    def __getitem__(self, key):
        if self._lock:
            if key in self._data1:
                return self._data1[key]
        else:
            if key in self._data:
                return copy.deepcopy(self._data[key])
    
    def __contains__(self, key):
        if self._lock:
            return key in self._data1
        else:
            return key in self._data


if __name__ == '__main__':

    with FragileDict() as d:
        d['key'] = 6
        print(d['key'])
        d['ord'] = 7
        print('ord' in d and d['ord'] == 7)
