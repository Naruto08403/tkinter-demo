import tkinter as tk
import random

# Game settings
GAME_WIDTH = 600
GAME_HEIGHT = 400
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"
SNAKE_SIZE = 20
SPEED = 100

# Initialize snake and food properties
snake_parts = [(60,0),(40,0),(20,0)]
snake_direction = "right"
food_position = (0, 0)
score = 0

# Initialize tkinter window
window = tk.Tk()
window.title("Snake Game")
canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

# Score label
score_label = tk.Label(window, text=f"Score: {score}", font=("Arial", 16), bg="black", fg="white")
score_label.pack()

# Spawn food
def spawn_food():
    global food_position
    food_x = random.randint(0, (GAME_WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
    food_y = random.randint(0, (GAME_HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
    food_position = (food_x, food_y)
    canvas.create_oval(food_x, food_y, food_x + SNAKE_SIZE, food_y + SNAKE_SIZE, fill=FOOD_COLOR, tags="food")



# Update snake position and handle game logic
def move_snake():
    global score

    # Calculate new head position
    head_x, head_y = snake_parts[0]
    if snake_direction == "up":
        head_y -= SNAKE_SIZE
    elif snake_direction == "down":
        head_y += SNAKE_SIZE
    elif snake_direction == "left":
        head_x -= SNAKE_SIZE
    elif snake_direction == "right":
        head_x += SNAKE_SIZE

    # Add new head position
    new_head = (head_x, head_y)
    snake_parts.insert(0, new_head)
    

    # Check for collision with food
    if new_head == food_position:
        score += 1
        score_label.config(text=f"Score: {score}")
        canvas.delete("food")
        spawn_food()
        
    else:
        # Remove last segment of snake (move forward)
        last_part = snake_parts.pop()
        canvas.delete(str(last_part))
        canvas.update()
        

    # Check for collisions with wall or self
    if (head_x < 0 or head_x >= GAME_WIDTH or head_y < 0 or head_y >= GAME_HEIGHT or new_head in snake_parts[1:]):
        game_over()
        return

    # Draw the new snake
    for head_x,head_y in snake_parts:
        tag = str((head_x,head_y))
        canvas.create_rectangle(
            head_x, head_y, head_x + SNAKE_SIZE, head_y + SNAKE_SIZE,
            fill=SNAKE_COLOR, tags=[tag]
        )
    
    window.after(SPEED, move_snake)

# Game over function
def game_over():
    canvas.create_text(
        GAME_WIDTH // 2, GAME_HEIGHT // 2,
        text="GAME OVER", font=("Arial", 24), fill="red"
    )

# Control the snake
def change_direction(new_direction):
    global snake_direction
    # Prevent snake from reversing
    if new_direction == "up" and snake_direction != "down":
        snake_direction = "up"
    elif new_direction == "down" and snake_direction != "up":
        snake_direction = "down"
    elif new_direction == "left" and snake_direction != "right":
        snake_direction = "left"
    elif new_direction == "right" and snake_direction != "left":
        snake_direction = "right"

# Key bindings
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))

# Start the game
spawn_food()
move_snake()
window.mainloop()
