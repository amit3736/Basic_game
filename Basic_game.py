import tkinter as tk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        # Create a canvas to draw the board and pieces
        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack()

        # Draw the grid lines
        self.canvas.create_line(100, 0, 100, 300, fill="black", width=3)
        self.canvas.create_line(200, 0, 200, 300, fill="black", width=3)
        self.canvas.create_line(0, 100, 300, 100, fill="black", width=3)
        self.canvas.create_line(0, 200, 300, 200, fill="black", width=3)

        # Initialize game variables
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        # Bind click events to the canvas
        self.canvas.bind("<Button-1>", self.click)

    def click(self, event):
        x, y = event.x, event.y
        row, col = y // 100, x // 100

        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player

            if self.current_player == "X":
                self.canvas.create_line(col * 100 + 20, row * 100 + 20, col * 100 + 80, row * 100 + 80, fill="blue", width=3)
                self.canvas.create_line(col * 100 + 20, row * 100 + 80, col * 100 + 80, row * 100 + 20, fill="blue", width=3)
            else:
                self.canvas.create_oval(col * 100 + 20, row * 100 + 20, col * 100 + 80, row * 100 + 80, fill="red", outline="red", width=3)

            self.current_player = "O" if self.current_player == "X" else "X"

            # Check for a win or a tie
            if self.check_win():
                self.game_over(f"{self.current_player} wins!")
            elif self.check_tie():
                self.game_over("It's a tie!")

    def check_win(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def check_tie(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def game_over(self, message):
        self.canvas.create_text(150, 150, text=message, font=("Arial", 20), fill="black")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
