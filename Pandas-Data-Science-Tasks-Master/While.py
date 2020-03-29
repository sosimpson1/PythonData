secret_word = " giraffe"
guess = " "
guess_count = 0

while guess != secret_word:
      guess = input(" Enter guess: ")
      guess_count += 1

print("You win!")