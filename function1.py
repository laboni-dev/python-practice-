# লাবনীর প্রথম Function Factory 🏭💚

def greet_queen():
    print("Good Morning Data Queen 👑")
    print("আজকে Function শিখবি 🔥")

def calculate_total(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total

def calculate_average(total, subjects):
    average = total / subjects
    return average

def show_grade(avg):
    if avg >= 90:
        print("Grade: A+ 👑 Loop Queen")
    elif avg >= 80:
        print("Grade: A ⭐ Game Dev")
    else:
        print("Grade: B 💚 Keep Grinding")

# এবার Function গুলো Call করি 👇
greet_queen()

laboni_marks = [85, 92, 78, 90, 88]
print("\nলাবনীর মার্কস:", laboni_marks)

total = calculate_total(laboni_marks)
print(f"Total: {total}/500")

avg = calculate_average(total, 5)
print(f"Average: {avg}%")

show_grade(avg)
print("\n[Program finished] 🎉")