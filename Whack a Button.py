import tkinter as tk
import random
import os

# Setup
window = tk.Tk()
window.title("Whack-a-Button")
window.geometry("400x400")
window.iconbitmap("icon.ico")


score = 0
time_left = 30
high_score = 0
button_sizes = [12, 10, 8, 6]

# Load high score
if os.path.exists("high_score.txt"):
    with open("high_score.txt", "r") as f:
        high_score = int(f.read())

# Labels
score_label = tk.Label(window, text=f"Score: {score}", font=("Arial", 14))
score_label.pack()

timer_label = tk.Label(window, text=f"Time: {time_left}", font=("Arial", 14))
timer_label.pack()

high_score_label = tk.Label(window, text=f"High Score: {high_score}", font=("Arial", 12))
high_score_label.pack()

# Button
btn = tk.Button(window, text="Whack me!", font=("Arial", 12), command=lambda: whack())
btn.place(x=150, y=150)

# Control Buttons
def start_game():
    global score, time_left
    score = 0
    time_left = 30
    score_label.config(text=f"Score: {score}")
    timer_label.config(text=f"Time: {time_left}", fg="black")
    btn.config(state="normal")
    move_button()
    countdown()

def reset_game():
    global score, time_left
    score = 0
    time_left = 30
    score_label.config(text=f"Score: {score}")
    timer_label.config(text=f"Time: {time_left}", fg="black")
    btn.place(x=150, y=150)
    btn.config(font=("Arial", 12), state="normal")

start_btn = tk.Button(window, text="Start", command=start_game)
start_btn.pack()

reset_btn = tk.Button(window, text="Reset", command=reset_game)
reset_btn.pack()

# Game Logic
def whack():
    global score, high_score
    score += 1
    score_label.config(text=f"Score: {score}")
    move_button()

    # Shrink button based on score
    size_index = min(score // 5, len(button_sizes)-1)
    btn.config(font=("Arial", button_sizes[size_index]))

    if score > high_score:
        high_score = score
        high_score_label.config(text=f"High Score: {high_score}")
        with open("high_score.txt", "w") as f:
            f.write(str(high_score))

def move_button():
    x = random.randint(50, 350)
    y = random.randint(100, 300)
    btn.place(x=x, y=y)

def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1

        # Animate countdown color
        if time_left <= 5:
            timer_label.config(fg="red")
        elif time_left <= 10:
            timer_label.config(fg="orange")
        else:
            timer_label.config(fg="black")

        timer_label.config(text=f"Time: {time_left}")
        window.after(1000, countdown)
    else:
        btn.config(state="disabled")
        btn.config(text="Game Over")

window.mainloop()