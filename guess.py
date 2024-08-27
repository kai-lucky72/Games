import random
secret_number = random.randint(1,20)
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess =int(input("Guess:"))
    guess_count+=1
    if guess==secret_number:
        print("Congratulations!")
        break
else:
    print("you failed")
    print("the secret number was ",secret_number)
