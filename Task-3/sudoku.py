import tkinter as tk
from tkinter import messagebox
import numpy as np

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.grid = np.zeros((9, 9), dtype=int)
        self.create_widgets()

    def create_widgets(self):
        self.entries = [[tk.Entry(self.root, width=3, font=('Arial', 18), justify='center') for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.entries[i][j].grid(row=i, column=j)
        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.grid(row=9, column=0, columnspan=9)
        self.load_button = tk.Button(self.root, text="Load", command=self.load_grid)
        self.load_button.grid(row=10, column=0, columnspan=9)

    def load_grid(self):
        for i in range(9):
            for j in range(9):
                value = self.entries[i][j].get()
                if value.isdigit():
                    self.grid[i, j] = int(value)

    def is_valid(self, row, col, num):
        if num in self.grid[row, :] or num in self.grid[:, col]:
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        if num in self.grid[start_row:start_row + 3, start_col:start_col + 3]:
            return False
        return True

    def find_empty_location(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i, j] == 0:
                    return (i, j)
        return None

    def solve_sudoku(self):
        empty_location = self.find_empty_location()
        if not empty_location:
            return True
        row, col = empty_location
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.grid[row, col] = num
                if self.solve_sudoku():
                    return True
                self.grid[row, col] = 0
        return False

    def solve(self):
        self.load_grid()
        if self.solve_sudoku():
            self.update_gui()
        else:
            messagebox.showinfo("Result", "No solution exists")

    def update_gui(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, str(self.grid[i, j]))

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()
