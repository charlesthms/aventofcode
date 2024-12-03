import re

class Solver:
    def __init__(self) -> None:
        self.file = open("input.txt", "r").read().strip()

    def detect(self, l):
        match = re.match(r"\((\d{1,3}),(\d{1,3})\)", l)
        if match is not None:
            return int(match.group(1))*int(match.group(2))
        return 0

    def first(self) -> int:
        return sum(self.detect(i) for i in self.file.split("mul"))

    def second(self) -> int:
        res = 0
        do = True
        for i in range(len(self.file)):
            if self.file[i:].startswith("do()"):
                do=True
            if self.file[i:].startswith("don't()"):
                do=False
            match = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", self.file[i:])
            if match is not None and do:
                res += int(match.group(1))*int(match.group(2))
        return res

if __name__ == "__main__":
    s = Solver()
    print(f"Part 1: {s.first()}")
    print(f"Part 2: {s.second()}")
