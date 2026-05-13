# লাবনীর মার্কশিট 💚
marks = [85, 92, 78, 90, 88]
subjects = ["Bangla", "English", "Math", "Science", "Computer"]

print("লাবনীর রেজাল্ট 👑")
print("---------------")

total = 0

for i in range(5):
    print(f"{subjects[i]}: {marks[i]}")
    total = total + marks[i]

average = total / 5

print("---------------")
print(f"Total Marks: {total}/500")
print(f"Average: {average}")
print(f"Percentage: {average}%")

if average >= 90:
    print("Grade: A+ 👑 Loop Queen")
elif average >= 80:
    print("Grade: A ⭐ Game Dev")
else:
    print("Grade: B 💚 Keep Grinding")