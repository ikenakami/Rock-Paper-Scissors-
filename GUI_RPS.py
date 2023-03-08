import tkinter as tk
import random

root = tk.Tk()
root.title("Rock, Paper, Scissors")


player_score = 0
cpu_score = 0
ties = 0
total_games = 0

title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Times", 16,"bold"))
title_label.pack(pady=10)

player_counter = tk.Label(root, text="Total Player Wins: {}".format(player_score),font=("Times"))
player_counter.pack()

cpu_counter = tk.Label(root, text="Total CPU Wins: {}".format(cpu_score),font=("Times"))
cpu_counter.pack()

tie_counter = tk.Label(root, text="Total Ties: {}".format(ties),font=("Times"))
tie_counter.pack()

total_counter = tk.Label(root, text="Total Games: {}".format(total_games),font=("Times"))
total_counter.pack()

result_label = tk.Label(root, text="",font=("Times"))
result_label.pack(pady=10)


rock_button = tk.Button(root, text="Rock", command=lambda: play_game("Rock"))
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play_game("Paper"))
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("Scissors"))
scissors_button.pack(side=tk.LEFT, padx=10)

def play_game(user_choice):
    global player_score, cpu_score, ties, total_games
    cpu_choice = random.choice(["Rock", "Paper", "Scissors"])
    total_games += 1
    if user_choice == cpu_choice:
        result = "It's a tie "
        ties += 1
    elif user_choice == "Rock":
        if cpu_choice == "Paper":
            result = "You lose \n {} wraps {}".format(cpu_choice, user_choice)
            cpu_score += 1
        else:
            result = "You win \n {} breaks {}".format(user_choice, cpu_choice)
            player_score += 1
    elif user_choice == "Paper":
        if cpu_choice == "Scissors":
            result = "You lose \n {} slashes {}".format(cpu_choice, user_choice)
            cpu_score += 1
        else:
            result = "You win \n {} wraps {}".format(user_choice, cpu_choice)
            player_score += 1
    elif user_choice == "Scissors":
        if cpu_choice == "Rock":
            result = "You lose \n {} breaks {}".format(cpu_choice, user_choice)
            cpu_score += 1
        else:
            result = "You win \n {} slashes {}".format(user_choice, cpu_choice)
            player_score += 1
    update_counters()
    result_label.config(text=result)


def update_counters():
    player_counter.config(text="Total Player Wins: {}".format(player_score),font=("Times"))
    cpu_counter.config(text="Total CPU Wins: {}".format(cpu_score),font=("Times"))
    tie_counter.config(text="Total Ties: {}".format(ties),font=("Times"))
    total_counter.config(text="Total Games: {}".format(total_games),font=("Times"))

root.mainloop()

