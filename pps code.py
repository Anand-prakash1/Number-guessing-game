#Number guessing game 
Name = "Anand prakash"
admission_no = 23131040126
print(Name)
print(admission_no)

actual_number = 46
attempt = 0

while True:
    guess_number = int(input("Guess the first number: "))
    guess_number = int(input("Guess the second number: "))
    guess_number = int(input("Guess the third number: "))
    attempt += 1
    if guess_number < actual_number:
        print("Your number was too low")
    elif guess_number > actual_number:
        print("Your number was too high")
    elif guess_number == actual_number:
        print(f"Congrats your guess was right in {attempt} attempt")
