import random

# List of friends
friends = ['hamza', 'ali', 'talha', 'muawia', 'zakria', 'babur']

# Choose a random word
chosen_friend = random.choice(friends)

# Placeholder for the word
placeholder = ['_'] * len(chosen_friend)

# Number of attempts = length of the chosen word
attempts = len(chosen_friend)
game_over = False

print(f"Word to guess: {' '.join(placeholder)}")
print(f"You have {attempts} attempts.")

# Game loop
while not game_over and attempts > 0:
    letter_guess = input("Guess a letter: ").lower()

    if letter_guess in chosen_friend:
        for index in range(len(chosen_friend)):
            if chosen_friend[index] == letter_guess:
                placeholder[index] = letter_guess
    else:
        print("Incorrect guess!")

    attempts -= 1  # Reduce attempts after each guess
    print(f"Word: {' '.join(placeholder)} | Attempts left: {attempts}")

    # Check if player has won
    if "_" not in placeholder:
        print(f"🎉 Congratulations! You guessed the word: {chosen_friend}")
        game_over = True

# If attempts run out and word is not fully guessed
if "_" in placeholder:
    print(f"❌ Game Over! The correct word was: {chosen_friend}")
