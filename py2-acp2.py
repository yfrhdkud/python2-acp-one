numbers = list(range(1, 51))

index = id(numbers) % len(numbers)
chosen_number = numbers[index]

print("One of these numbers are correct, guess the number.")
print(numbers)

while True:
    try:
        guess = int(input("Guess the number: "))
        if guess == chosen_number:
            print("Correct, You guessed the number.")
            break
        elif guess in numbers:
            if abs(guess - chosen_number) <= 5:
                print("Close, try again")
            else:
                print("Wrong guess, Try again.")
        else:
            print("This number is not on the list.")
    except ValueError:
        print("This is not a number")