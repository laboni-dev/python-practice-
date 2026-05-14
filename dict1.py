# লাবনীর প্রথম Dictionary 👑📊
# Data কে নাম-ঠিকানা দেওয়া

# Day 5 এ List ছিল: [name, total, avg]
# Day 6 এ Dictionary: সবকিছুর নাম আছে

laboni = {
    "name": "Laboni Dev",
    "roll": 1,
    "class": "Python Boss Level",
    "marks": {
        "Bangla": 95,
        "English": 99,
        "Math": 89,
        "Science": 85,
        "Computer": 80
    },
    "total": 451,
    "average": 90.2,
    "grade": "A+",
    "title": "Class Topper 👑",
    "skills": ["Loop", "List", "Function", "Dictionary"]
}

# Dictionary থেকে Data বের করা
print("🎓 STUDENT PROFILE 🎓")
print("=" * 30)
print(f"Name: {laboni['name']}")
print(f"Roll: {laboni['roll']}")
print(f"Title: {laboni['title']}")
print(f"Total: {laboni['total']}/500")
print(f"Average: {laboni['average']}%")
print(f"Grade: {laboni['grade']}")
print("=" * 30)

print("\n📚 SUBJECT MARKS 📚")
for subject in laboni["marks"]:
    mark = laboni["marks"][subject]
    print(f"{subject}: {mark}")

print("\n💚 SKILLS UNLOCKED 💚")
for i in range(len(laboni["skills"])):
    print(f"{i+1}. {laboni['skills'][i]}")

print("\n[Program finished] 🎉")