# roulette_backend.py
import random
import time

class RussianRouletteBackend:
    def __init__(self):
        self.prize_tiers = [10000, 25000, 50000, 100000, 250000, 500000]
        self.current_round = 0
        self.current_prize = self.prize_tiers[0]
        self.hints_used = 0
        self.bullet = random.randint(1, 6)

    def get_hint(self):
        if self.hints_used >= 2:
            return "No more hints available!", False
        
        # Reduce prize by 20%, but not below $1,000
        self.current_prize = max(1000, int(self.current_prize * 0.8))
        hints = [
            f"The number is {'odd' if self.bullet % 2 == 1 else 'even'}",
            f"The number is {'greater than' if self.bullet > 3 else 'less than or equal to'} 3",
            f"The number is {'divisible by 2' if self.bullet % 2 == 0 else 'not divisible by 2'}"
        ]
        hint = random.choice(hints)
        self.hints_used += 1
        return hint, True

    def check_guess(self, guess):
        try:
            guess = int(guess)
            if guess < 1 or guess > 6:
                return "Please enter a number between 1 and 6!", False, False
        except ValueError:
            return "Invalid input! Enter a number.", False, False

        # Simulate tension (returning messages for frontend to display)
        time.sleep(1)
        spinning_msg = "Spinning the chamber..."
        time.sleep(1)
        click_msg = "Click..."

        if guess == self.bullet:
            win_msg = f"Survived! The number was {self.bullet}."
            return [spinning_msg, click_msg, win_msg], True, True
        else:
            lose_msg = f"BANG! You lost. The number was {self.bullet}."
            return [spinning_msg, click_msg, lose_msg], True, False

    def next_round(self):
        if self.current_round < len(self.prize_tiers) - 1:
            self.current_round += 1
            self.current_prize = self.prize_tiers[self.current_round]
            self.hints_used = 0
            self.bullet = random.randint(1, 6)
            return True
        return False

    def get_current_prize(self):
        return self.current_prize

    def get_max_rounds(self):
        return len(self.prize_tiers)
    