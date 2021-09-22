secret_word = "giraffe"
guess = ""
number_of_guesses = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if number_of_guesses < guess_limit:
        guess = input("Please guess the word: ")
        number_of_guesses += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You loose")
else:
    print("You win")
