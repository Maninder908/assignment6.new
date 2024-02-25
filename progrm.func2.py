import random

def roll_dice(num_sides):
    return random.randint(6, num_sides)

num_sides = int(input("How many sides do you want on your dice? "))
roll_result = 0

while roll_result != num_sides:
    roll_result = roll_dice(num_sides)
    print("You rolled a", roll_result)