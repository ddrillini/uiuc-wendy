class Params:
    def __init__(self):
        self.dict = []

    def __getitem__(self, x):
        if type(x) is int:
            return self.index(x)
        if type(x) is str:
            return self.get(x)
        raise Exception("Bad type index")

    def __len__(self):
        return len(self.dict)

    def __contains__(self, x):
        if type(x) == tuple and len(x) == 2:
            if type(x[0]) == str and type(x[1]) == str:
                return x in self.dict
        if type(x) == str:
            for k,v in self.dict:
                if k == x:
                    return True
            return False
        raise Exception("Bad search type")

    def add(self, param, value):
        if (not type(param) is str) or (not type(value) is str):
            raise Exception("Parameters must be strings")
        self.dict.append((param, value))

    def index(self, i):
        return self.dict[i]

    def get(self, x):
        ret = []
        for k,v in self.dict:
            if k == x:
                ret.append(v)
        return ret
