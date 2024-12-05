import re

class Solver:
    def __init__(self) -> None:
        with open("input.txt", "r") as file:
            self.grid = [line.strip() for line in file.readlines()]
        self.word = "XMAS"
        self.word_reversed = self.word[::-1]
        self.grid_size = len(self.grid)


    def find_horizontal(self):
        return sum([row.count(self.word) + row.count(self.word_reversed) for row in self.grid])

    def find_vertical(self):
        cols = ["".join(row[col] for row in self.grid) for col in range(self.grid_size)]

        return sum([col.count(self.word) + col.count(self.word_reversed) for col in cols])

    def find_diagonals(self):
        diags1 = []
        diags2 = []

        for d in range(-self.grid_size + 1, self.grid_size):
            diag = ""
            for i in range(max(0, d), min(self.grid_size, self.grid_size + d)):
                diag += self.grid[i][i - d]
            diags1.append(diag)

        for d in range(-self.grid_size + 1, self.grid_size):
            diag = ""
            for i in range(max(0, d), min(self.grid_size, self.grid_size + d)):
                diag += self.grid[i][(self.grid_size - 1) - (i - d)]
            diags2.append(diag)

        return sum([diag.count(self.word) + diag.count(self.word_reversed) for diag in diags1+diags2])

    def first(self) -> int:
        total_count = 0
        total_count += self.find_horizontal()
        total_count += self.find_vertical()
        total_count += self.find_diagonals()
        return total_count


    def is_xmas(self, row: int, col: int) -> bool:

        if self.grid[row][col] != "A":
            return False

        top_left = self.grid[row - 1][col - 1]
        top_right = self.grid[row - 1][col + 1]
        bottom_left = self.grid[row + 1][col - 1]
        bottom_right = self.grid[row + 1][col + 1]

        diag1 = (top_left, self.grid[row][col], bottom_right)
        diag2 = (top_right, self.grid[row][col], bottom_left)

        return self.is_mas_pattern(diag1) and self.is_mas_pattern(diag2)

    def is_mas_pattern(self, diag) -> bool:
        return diag == ("M", "A", "S") or diag == ("S", "A", "M")

    def second(self) -> int:
        return sum(
            self.is_xmas(row, col)
            for row in range(1, self.grid_size - 1)
            for col in range(1, self.grid_size - 1)
        )

if __name__ == "__main__":
    s = Solver()
    print(f"Part 1: {s.first()}")
    print(f"Part 2: {s.second()}")
