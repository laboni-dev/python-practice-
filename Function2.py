# লাবনীর Marksheet App 📊👑
# Function + Input = Real World Project

def get_marks():
    marks = []
    subjects = ["Bangla", "English", "Math", "Science", "Computer"]

    print("5টা Subject এর মার্কস দাও 👇")
    for sub in subjects:
        mark = int(input(f"{sub}: "))
        marks.append(mark)
    return marks, subjects

def calculate_total(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total

def calculate_average(total, count):
    return total / count

def find_highest(marks, subjects):
    highest = marks[0]
    high_sub = subjects[0]
    for i in range(len(marks)):
        if marks[i] > highest:
            highest = marks[i]
            high_sub = subjects[i]
    return high_sub, highest

def show_result(name, marks, subjects, total, avg, high_sub, highest):
    print(f"\n{name} এর রেজাল্ট 👑")
    print("-----------------")
    for i in range(len(marks)):
        print(f"{subjects[i]}: {marks[i]}")
    print("-----------------")
    print(f"Total: {total}/500")
    print(f"Average: {avg}%")
    print(f"Highest: {high_sub} = {highest} 🔥")

    if avg >= 90:
        print("Grade: A+ 👑 Loop Queen")
    elif avg >= 80:
        print("Grade: A ⭐ Game Dev")
    else:
        print("Grade: B 💚 Keep Grinding")

# Main Program শুরু 👇
print("🎓 Marksheet Generator 🎓")
name = input("Student এর নাম: ")

marks, subjects = get_marks()
total = calculate_total(marks)
avg = calculate_average(total, len(marks))
high_sub, highest = find_highest(marks, subjects)

show_result(name, marks, subjects, total, avg, high_sub, highest)
print("\n[Program finished] 🎉")