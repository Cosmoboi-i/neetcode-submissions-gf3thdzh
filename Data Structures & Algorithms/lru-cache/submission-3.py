class LRUCache:

    def __init__(self, capacity: int):
        self.table = {}
        self.cap = capacity
        self.maxx = 0
        self.maxxKey = None

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        
        val = self.table[key]['val']
        usage = self.table[key]['usage']
        self.table[key]['usage'] = max(self.maxx, usage) + 1
        self.maxx = max(self.maxx, usage) + 1
        self.maxxKey = key
        print(self.table)
        return val


    def put(self, key: int, value: int) -> None:
        if self.cap == 0 and key not in self.table:
            least = self.maxx
            leastKey = self.maxxKey
            for x in self.table.keys():
                usage = self.table[x]['usage']
                if least > usage:
                    least = min(usage, least)
                    leastKey = x
            print(leastKey)
            self.table.pop(leastKey)
            self.cap += 1

        if key not in self.table:
            self.cap -= 1

        usage = self.maxx + 1
        self.maxx = usage
        self.maxxKey = key
        self.table[key] = {'val': value, 'usage': usage}


        print(self.table)
