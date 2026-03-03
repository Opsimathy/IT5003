class SpecialStack:
    def __init__(self):
        self.s = []
        self.m = []

    def peek(self) -> int:
        return self.s[-1] if self.s else -1

    def pop(self) -> int:
        if not self.s:
            return -1
        if self.m:
            self.m.pop()
        return self.s.pop()

    def push(self, value: int) -> None:
        self.s.append(value)
        if self.m:
            self.m.append(min(value, self.m[-1]))
        else:
            self.m.append(value)

    def findMin(self) -> int:
        return self.m[-1] if self.m else -1


if __name__ == "__main__":
    S = SpecialStack()
    assert S.peek() == -1
    assert S.findMin() == -1
    for x in [2, 7, 8, 6, 1, 5, 1]:
        S.push(x)
    assert S.peek() == 1
    assert S.findMin() == 1
    assert S.pop() == 1
    assert S.peek() == 5
    assert S.findMin() == 1
    assert S.pop() == 5
    assert S.pop() == 1
    assert S.peek() == 6
    assert S.findMin() == 2
    print("Test cases are all executed correctly.")
