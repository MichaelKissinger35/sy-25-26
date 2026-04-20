

#Ask user for a number 1-10

#If the input is not the number, tell them is wrong, and ask user again anc check number`

#If the input is the number, tell them they are correct

#guesses need to go up to 5 max


secret = 7

guesses = 0

guess = int(input("Guess a number between 1 and 10: "))
if guess > 7:
    print("Too high! Try again.")
    guesses += 1
elif guess < 7:
    print("Too low! Try again.")
    guesses += 1
elif guess == 7:
    print("Correct! You win!")
    guesses += 1
