class DynamicArray:
    
    def __init__(self, capacity: int):
        self.myArray = [0] * capacity
        self.size = 0
        
    def get(self, i: int) -> int:
        return self.myArray[i]

    def set(self, i: int, n: int) -> None:
        self.myArray[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.getCapacity():
            self.resize()
        self.myArray[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.myArray[self.size]

    def resize(self) -> None:
        self.myArray += [None] * self.getCapacity()

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return len(self.myArray)