# roulette_frontend.py
import tkinter as tk
from tkinter import messagebox
from roulette_backend import RussianRouletteBackend

class RussianRouletteFrontend:
    def __init__(self, root):
        self.root = root
        self.root.title("Russian Roulette: Guess the Number")
        self.root.geometry("600x400")
        self.root.configure(bg="#2b2b2b")

        # Initialize backend
        self.game = RussianRouletteBackend()

        # GUI Elements
        self.title_label = tk.Label(root, text="Russian Roulette", font=("Arial", 20, "bold"), bg="#2b2b2b", fg="red")
        self.title_label.pack(pady=10)

        self.prize_label = tk.Label(root, text=f"Current Prize: ${self.game.get_current_prize():,}", font=("Arial", 14), bg="#2b2b2b", fg="white")
        self.prize_label.pack(pady=5)

        self.instruction_label = tk.Label(root, text="Guess a number between 1 and 6", font=("Arial", 12), bg="#2b2b2b", fg="white")
        self.instruction_label.pack(pady=5)

        self.hint_label = tk.Label(root, text="", font=("Arial", 10, "italic"), bg="#2b2b2b", fg="yellow")
        self.hint_label.pack(pady=5)

        self.guess_entry = tk.Entry(root, font=("Arial", 12), width=5, justify="center")
        self.guess_entry.pack(pady=10)

        self.guess_button = tk.Button(root, text="Pull the Trigger", command=self.check_guess, font=("Arial", 12), bg="#ff4444", fg="white")
        self.guess_button.pack(pady=5)

        self.hint_button = tk.Button(root, text="Get Hint (-20% Prize)", command=self.get_hint, font=("Arial", 10), bg="#888888", fg="white")
        self.hint_button.pack(pady=5)

        self.status_label = tk.Label(root, text="", font=("Arial", 12), bg="#2b2b2b", fg="white")
        self.status_label.pack(pady=10)

    def get_hint(self):
        hint, success = self.game.get_hint()
        self.hint_label.config(text=f"Hint: {hint}" if success else hint)
        if success:
            self.prize_label.config(text=f"Current Prize: ${self.game.get_current_prize():,}")

    def check_guess(self):
        messages, valid, won = self.game.check_guess(self.guess_entry.get())
        
        if not valid:
            self.status_label.config(text=messages)
            return

        # Display tension messages
        for msg in messages[:-1]:  # All but the final result
            self.status_label.config(text=msg)
            self.root.update()
        
        self.guess_button.config(state="disabled")
        self.hint_button.config(state="disabled")
        self.status_label.config(text=messages[-1])  # Final result
        self.root.update()

        if won:
            if self.game.current_round < self.game.get_max_rounds() - 1:
                self.ask_to_continue()
            else:
                messagebox.showinfo("Winner!", f"You've won the max prize: ${self.game.get_current_prize():,}!")
                self.root.quit()
        else:
            messagebox.showwarning("Game Over", "You lost. Our Mercenaries are coming to your house.\n"
                                               "Please do not avoid, otherwise we will hunt for your family and your closest regards. Cheers.")
            self.root.quit()

    def ask_to_continue(self):
        response = messagebox.askyesno("Continue?", f"You won ${self.game.get_current_prize():,}! Risk it for ${self.game.prize_tiers[self.game.current_round + 1]:,}?")
        if response:
            self.game.next_round()
            self.prize_label.config(text=f"Current Prize: ${self.game.get_current_prize():,}")
            self.hint_label.config(text="")
            self.status_label.config(text="")
            self.guess_entry.delete(0, tk.END)
            self.guess_button.config(state="normal")
            self.hint_button.config(state="normal")
        else:
            messagebox.showinfo("Smart Choice", f"You walk away with ${self.game.get_current_prize():,}!")
            self.root.quit()

def start_game():
    root = tk.Tk()
    app = RussianRouletteFrontend(root)
    root.mainloop()

if __name__ == "__main__":
    start_game()