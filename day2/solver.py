class Solver:
    def __init__(self) -> None:
        self.file = open("input.txt", "r")
        self.lines = self.process_data()

    def process_data(self):
        lines = [line.strip().split() for line in self.file]
        lines = [[int(num) for num in sublist] for sublist in lines]
        return lines

    def check_first(self, l):
        is_increasing = all(a<b and abs(a-b)<=3 for a,b in zip(l, l[1:]))
        is_decreasing = all(a>b and abs(a-b)<=3 for a,b in zip(l, l[1:]))
        return is_increasing or is_decreasing

    def first(self) -> int:
        return sum(1 for line in self.lines if self.check_first(line))

    def check_second(self, l: list):
        if not self.check_first(l):
            for i in range(len(l)):
                tmp = l[:i] + l[i + 1:]
                if self.check_first(tmp):
                    return 1
        return 0

    def second(self) -> int:
        return sum(self.check_second(l) for l in self.lines) + self.first()

if __name__ == "__main__":
    s = Solver()
    print(f"Part 1: {s.first()}")
    print(f"Part 2: {s.second()}")
