# লাবনীর Class Topper Finder v2.0 🏆💳
# Dictionary + Function + Loop = Clean Software

def get_student_data():
    name = input("\nStudent এর নাম (শেষ করতে 'done' লেখো): ")
    if name.lower() == 'done':
        return None

    marks = {}
    subjects = ["Bangla", "English", "Math", "Science", "Computer"]
    print(f"{name} এর মার্কস দাও 👇")
    for sub in subjects:
        mark = int(input(f"{sub}: "))
        marks[sub] = mark # Dictionary তে Add করছি
    return name, marks

def calculate_result(marks_dict):
    total = sum(marks_dict.values()) # Dictionary এর সব Value যোগ
    avg = total / len(marks_dict)
    return total, avg

def find_class_topper(all_students):
    topper = max(all_students, key=lambda x: x["average"])
    # max() + lambda = এক লাইনে Topper বের করা 😭🔥
    return topper

def show_class_result(all_students):
    print("\n\n📊 CLASS RESULT SHEET v2.0 📊")
    print("=" * 50)
    for student in all_students:
        print(f"{student['name']}: Total={student['total']}, Avg={student['average']}%")
    print("=" * 50)

# Main Program 👇
print("🏆 CLASS TOPPER FINDER v2.0 - Dictionary Edition 🏆")
all_students = []

while True:
    data = get_student_data()
    if data == None:
        break

    name, marks_dict = data
    total, avg = calculate_result(marks_dict)

    # Student কে Dictionary বানিয়ে List এ ঢোকাচ্ছি
    student = {
        "name": name,
        "marks": marks_dict,
        "total": total,
        "average": round(avg, 2)
    }
    all_students.append(student)
    print(f"{name} এর Data Save হলো ✅")

if len(all_students) > 0:
    show_class_result(all_students)
    topper = find_class_topper(all_students)

    print(f"\n🥇 CLASS TOPPER: {topper['name']} 👑")
    print(f"Average: {topper['average']}% 🔥")
    print(f"Total: {topper['total']}/500")
    print("\nTopper এর Subject-wise Marks:")
    for sub, mark in topper["marks"].items():
        print(f"{sub}: {mark}")
else:
    print("\nকোনো Student এর Data দেওয়া হয়নি 😅")

print("\n[Program finished] 🎉")