class OrderedStream:

    def __init__(self, n: int):
        self.data = [None]*n
        self.iden = 0

    def insert(self, id: int, value: str) -> List[str]:
        id -= 1
        self.data[id] = value 
        if id > self.iden:
            return []  
        
        while self.iden < len(self.data) and self.data[self.iden]:
            self.iden += 1
        return self.data[id:self.iden]