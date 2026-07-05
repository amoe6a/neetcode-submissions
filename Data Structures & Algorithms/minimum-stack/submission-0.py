class MinStack:

    def __init__(self):
        self.s = []
        self.ss = []

    def push(self, value: int) -> None:
        self.s.append(value)
        if len(self.ss) >= 1:
            if value < self.ss[-1]:
                self.ss.append(value)
            else:
                self.ss.append(self.ss[-1])
        else:
            self.ss.append(value)

    def pop(self) -> None:
        self.s.pop()
        self.ss.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.ss[-1]