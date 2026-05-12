import random

secret = random.randint(1, 100)
guess = 0
tries = 0

print("Number Guessing Game 🎮 Level 2")
print("আমি 1 থেকে 100 এর মধ্যে একটা নাম্বার ভেবেছি।")
print("তুই কয় চান্সে পারিস দেখি 👑")

while guess != secret:
    guess = int(input("তোর Guess: "))
    tries = tries + 1  # কয়বার Try করলি গুনবে
    
    if guess < secret:
        print(f"আরো বড় হবে ⬆️ | Try: {tries}")
    elif guess > secret:
        print(f"আরো ছোট হবে ⬇️ | Try: {tries}")
    else:
        print(f"সাব্বাশ! {tries} চান্সে মিলে গেছে 🎉")

print(f"Game Over. তুই মোট {tries} বারে জিতে গেলি 👑")