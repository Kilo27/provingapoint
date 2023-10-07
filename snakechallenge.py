import tkinter as tk
import random

# Constants
WIDTH = 1920
HEIGHT = 1080
GRID_SIZE = 20
DELAY = 100

class SnakeGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Snake Challenge")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.canvas = tk.Canvas(self, bg="black", width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.snake = [(WIDTH/2, HEIGHT/2)]
        self.direction = (0, -1)
        self.food = self.generate_food()
        self.bind("<KeyPress>", self.on_keypress)
        self.after(DELAY, self.move_snake)

    def generate_food(self):
        """Generate food at a random location."""
        x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        return x, y

    def draw_snake(self):
        """Draw the snake on the canvas."""
        self.canvas.delete("snake")
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(
                x, y, x + GRID_SIZE, y + GRID_SIZE, fill="green", tags="snake"
            )

    def draw_food(self):
        """Draw the food on the canvas."""
        x, y = self.food
        self.canvas.create_oval(
            x, y, x + GRID_SIZE, y + GRID_SIZE, fill="red", tags="food"
        )

    def move_snake(self):
        """Move the snake and update the game state."""
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0] * GRID_SIZE, head_y + self.direction[1] * GRID_SIZE)
        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.canvas.delete("food")
            self.food = self.generate_food()
        else:
            self.snake.pop()

        if (
            new_head[0] < 0
            or new_head[0] >= WIDTH
            or new_head[1] < 0
            or new_head[1] >= HEIGHT
        ):
            self.game_over()
            return

        if new_head in self.snake[1:]:
            self.game_over()
            return

        self.draw_snake()
        self.draw_food()

        self.after(DELAY, self.move_snake)

    def game_over(self,):
        """Game over handling."""
        self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2, text="Game Over!, Press R to Restart", fill="white", font=("Helvetica", 24)
        )
        self.direction = (0, 0)

    def on_keypress(self, event):
        """Handle arrow key presses."""
        if event.keysym == "Up":
            self.direction = (0, -1)
        elif event.keysym == "Down":
            self.direction = (0, 1)
        elif event.keysym == "Left":
            self.direction = (-1, 0)
        elif event.keysym == "Right":
            self.direction = (1, 0)






if __name__ == "__main__":
    game = SnakeGame()
    game.mainloop()
