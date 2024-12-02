class Solver:
    def __init__(self) -> None:
        self.file = open("input.txt", "r")
        self.left, self.right = self.process_data()

    def process_data(self):
        left, right = [], []
        for line in self.file:
            left.append(int(line[:5].strip()))
            right.append(int(line[-6:].strip()))
        return left, right

    def first(self) -> int:
        self.left.sort()
        self.right.sort()
        return sum((abs(a-b) for a,b in zip(self.left, self.right)))

    def second(self) -> int:
        return sum((a*self.right.count(a) for a in self.left))

if __name__ == "__main__":
    s = Solver()
    print(f"Part 1: {s.first()}")
    print(f"Part 2: {s.second()}")
