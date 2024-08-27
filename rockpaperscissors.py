import random
import tkinter as tk

window = tk.Tk()


class Game:
    def __init__(self):
        self.user_choice = None
        self.computer_choice = None
        self.scoreboard = tk.Label(window, text="score: You 0 - Computer 0")

    def choice_rock(self):
        self.user_choice = "rock"
        self.play_game()

    def choice_paper(self):
        self.user_choice = "paper"
        self.play_game()

    def choice_scissor(self):
        self.user_choice = "scissor"
        self.play_game()

    # Inside the Game class
    def play_game(self):
        choices = ["rock", "paper", "scissor"]
        self.computer_choice = random.choice(choices)
        winner = self.determine_winner()
        self.change_scoreboard(winner)  # Call change_scoreboard to update the scoreboard
        result = f"You chose {self.user_choice}. Computer chose {self.computer_choice}. {winner}"
        tk.Label(window, text=result).pack()

    # The rest of the Game class remains unchanged

    def determine_winner(self):
        if self.user_choice == self.computer_choice:
            return "it's a tie bro!"
        elif self.user_choice == "rock":
            if self.computer_choice == "paper":
                return "computer wins!"
            else:
                return "you win!"
        elif self.user_choice == "paper":
            if self.computer_choice == "scissor":
                return "computer wins!"
            else:
                return "you win!"
        elif self.user_choice == "scissor":
            if self.computer_choice == "rock":
                return "computer wins!"
            else:
                return "you win!"

    def change_scoreboard(self, winner):
        try:
            you_score = int(self.scoreboard['text'].split("You")[1].split("-")[0].strip())
            computer_score = int(self.scoreboard['text'].split("Computer")[1].strip())
        except(IndexError, ValueError):
            print("Error: Unexpected error scoreboard format")

        if winner == "you win!":
            self.scoreboard.config(text=f"Score: You {you_score + 1} - Computer {computer_score}")
        elif winner == "computer wins!":
            self.scoreboard.config(text=f"Score: You {you_score} - Computer {computer_score + 1}")

game = Game()

button_rock = tk.Button(window, text="rock", command=game.choice_rock)
button_paper = tk.Button(window, text="paper", command=game.choice_paper)
button_scissor = tk.Button(window, text="scissor", command=game.choice_scissor)

game.scoreboard.pack()
button_rock.pack()
button_paper.pack()
button_scissor.pack()

window.mainloop()
