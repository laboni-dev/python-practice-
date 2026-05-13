# লাবনীর Class Topper Finder 🏆👑
# Function + Loop + List + Input = School Software

def get_student_data():
    name = input("\nStudent এর নাম (শেষ করতে 'done' লেখো): ")
    if name.lower() == 'done':
        return None

    marks = []
    subjects = ["Bangla", "English", "Math", "Science", "Computer"]
    print(f"{name} এর মার্কস দাও 👇")
    for sub in subjects:
        mark = int(input(f"{sub}: "))
        marks.append(mark)
    return name, marks

def calculate_total_avg(marks):
    total = sum(marks) # sum() = Python এর নিজের Function
    avg = total / len(marks)
    return total, avg

def find_class_topper(all_students):
    topper_name = ""
    topper_avg = 0

    for student in all_students:
        name = student[0]
        avg = student[2]
        if avg > topper_avg:
            topper_avg = avg
            topper_name = name
    return topper_name, topper_avg

def show_all_results(all_students):
    print("\n\n📊 CLASS RESULT SHEET 📊")
    print("=" * 40)
    for student in all_students:
        name, total, avg = student
        print(f"{name}: Total={total}, Average={avg}%")
    print("=" * 40)

# Main Program শুরু 👇
print("🏆 CLASS TOPPER FINDER 🏆")
all_students = [] # সব Student এর Data রাখবো

while True:
    data = get_student_data()
    if data == None: # User 'done' লিখেছে
        break

    name, marks = data
    total, avg = calculate_total_avg(marks)
    all_students.append([name, total, avg]) # List এর ভিতর List
    print(f"{name} এর Data Save হলো ✅")

# সব Student এর রেজাল্ট দেখাও
show_all_results(all_students)

# Class Topper বের করো
if len(all_students) > 0:
    topper_name, topper_avg = find_class_topper(all_students)
    print(f"\n🥇 CLASS TOPPER: {topper_name} 👑")
    print(f"Average: {topper_avg}% 🔥")
else:
    print("\nকোনো Student এর Data দেওয়া হয়নি 😅")

print("\n[Program finished] 🎉")