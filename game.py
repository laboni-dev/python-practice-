import random

secret = random.randint(1, 10)
guess = 0

print("Number Guessing Game 🎮")
print("আমি 1 থেকে 10 এর মধ্যে একটা নাম্বার ভেবেছি।")

while guess != secret:
    guess = int(input("তোর Guess: "))
    
    if guess < secret:
        print("আরো বড় হবে ⬆️")
    elif guess > secret:
        print("আরো ছোট হবে ⬇️")
    else:
        print("সাব্বাশ! মিলে গেছে 🎉")

print("Game Over. তুই জিতে গেলি 👑")