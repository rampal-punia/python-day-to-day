'''✨ Python: Dice Roll Outcomes ✨ 
🎲🎲🎲🎲🎲🎲🎲🎲

Get random output from a dice-roll
'''

import random

# Possible outcomes
outcomes = (1, 2, 3, 4, 5, 6)

# Method-1: Using choice from random module
score = random.choice(tuple(outcomes))
print(score)

# Method-2: Using randint from random module
score = random.randint(1, 6)
print(score)

# For more on Python follow: https://twitter.com/CodingMantras
