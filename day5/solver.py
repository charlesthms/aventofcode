from collections import defaultdict

class Solver:
    def __init__(self) -> None:
       with open("input.txt", "r") as file:
            self.data = file.read().split("\n\n")
            self.data = [el.split("\n") for el in self.data]
            self.rules = self.get_rules()
            self.updates = [[int(value) for value in update.split(",")] for update in self.data[1] if update]

    def get_rules(self):
        rules = defaultdict(list)
        lst = [[int(value) for value in el.split("|")] for el in self.data[0]]
        for pair in lst:
            rules[int(pair[0])].append(pair[1])
        return rules

    def first(self) -> int:
        sum = 0
        for update in self.updates:
            for i in range(len(update)):
                add = True
                if set(self.rules[update[i]]) & set(update[:i]):
                    add = False
                    break
            if add:
                sum += update[len(update) // 2]
        return sum

    def respect_rules(self, update):
        for i in range(len(update)):
            intersection = set(self.rules[update[i]]) & set(update[:i])
            if intersection:
                return i, intersection
        return None, None

    def swap(self, update, breaking_index, inter):
        for i in range(breaking_index):
            if update[i] in inter:
                update[i], update[breaking_index] = update[breaking_index], update[i]
                break

    def second(self) -> int:
        sum = 0
        for update in self.updates:
            breaking_index, inter = self.respect_rules(update)
            if breaking_index:
                while breaking_index is not None:
                    self.swap(update, breaking_index, inter)
                    breaking_index, inter = self.respect_rules(update)

                sum += update[len(update) // 2]

        return sum

if __name__ == "__main__":
    s = Solver()
    print(f"Part 1: {s.first()}")
    print(f"Part 2: {s.second()}")
