# Russian Roulette: Guess the Number
## A Game Where Your Luck Might Cost More Than Just Pride

Welcome to **Russian Roulette: Guess the Number**—a hilariously dark twist on "Guess the Number" that started as a late-night coding prank after too much coffee and a questionable Netflix binge. What began as a joke about mercenaries knocking on your door turned into a fully functional game with prizes, hints, and a GUI that’s just fancy enough to make you forget it’s still trying to send imaginary hitmen your way. Risk your virtual fortune for a shot at millions—or lose and face the consequences (don’t worry, it’s all in good fun… mostly).

### Features
- **Prizes**: Start at $10,000 and climb to a cool $500,000—if you’ve got the guts.
- **Hints**: Get a clue at the cost of 20% of your prize (because even in a game, nothing’s free).
- **GUI**: A sleek `tkinter` interface that’s one part casino, two parts horror movie vibe.
- **Mercenaries**: Lose, and our imaginary cleanup crew sends you a friendly note. Hide your cat.

### Prerequisites
- Python 3.x (because we’re not savages stuck in the 2.x era).
- `tkinter` (it’s built-in, so you’re already good to go).

### Installation
1. Clone or download this repo—or just copy-paste the files like a true rebel.
2. Make sure you have both `roulette_backend.py` and `roulette_frontend.py` in the same directory. The `README.md` is optional but highly recommended for street cred.

### How to Play: A Totally Serious Tutorial
So you’ve decided to tempt fate with a game that’s one part luck, one part masochism. Here’s how to survive (or not):

1. **Run the Game**  
   - Open your terminal, IDE, or whatever you use to pretend you’re a hacker.
   - Navigate to the folder with the files.
   - Type `python roulette_frontend.py` and hit Enter—or just click "Play" if you’re fancy with an IDE like PyCharm.
   - A window pops up. If it doesn’t, you’ve angered the Python gods. Try again.

2. **Understand the Screen**  
   - **Current Prize**: Starts at $10,000. That’s your imaginary yacht fund.
   - **Guess Entry**: A box where you type a number from 1 to 6. No decimals, no poetry—just numbers.
   - **Pull the Trigger**: The big red button. Click it to test your fate.
   - **Get Hint**: Gray button. Costs 20% of your prize to give you a nudge (e.g., “The number is odd”). Max 2 hints per round.
   - **Status Messages**: Tells you if you’re spinning, clicking, or about to meet the mercenaries.

3. **Gameplay**  
   - Type a number (1-6) in the box. Feeling lucky? Skip the hint. Feeling paranoid? Click “Get Hint” (your prize shrinks, but your odds improve).
   - Hit “Pull the Trigger.” The game spins the chamber, clicks, and decides your fate.
   - **Win**: You guessed right! The status says “Survived!” and you get a pop-up asking if you want to risk it for more cash.
     - Say “Yes” to go for the next prize tier (up to $500,000).
     - Say “No” to cash out like a coward—er, a wise soul.
   - **Lose**: Wrong guess? “BANG!” A pop-up warns that mercenaries are en route. Don’t panic—it’s just code.

4. **Hints Strategy**  
   - Hints cost 20% of your prize each time (e.g., $10,000 → $8,000 → $6,400). Prize won’t drop below $1,000, because we’re not *that* cruel.
   - Use them wisely—two hints max per round. They might say “The number is even” or “It’s greater than 3.”

5. **Winning Big**  
   - Survive all rounds to hit $500,000. You’ll get a smug “Winner!” pop-up. Frame it for your wall.
   - Quit anytime after a win to keep your current prize. No shame in running from imaginary hitmen.

6. **Losing**  
   - Guess wrong, and the game ends with a cheerful note about mercenaries hunting your family. Laugh it off—it’s all fake (we hope).

### Running the Game
- **One-Click Play**: Just run `roulette_frontend.py`. The backend connects automatically. No assembly required.
- **Files**: 
  - `roulette_backend.py`: The brains—handles prizes, hints, and the “bullet.”
  - `roulette_frontend.py`: The face—GUI
