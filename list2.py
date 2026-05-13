marks = [85, 92, 78, 90, 88]
subjects = ["Bangla", "English", "Math", "Science", "Computer"]

print("লাবনীর রেজাল্ট 👑")
print("---------------")

total = 0
highest = marks[0] # প্রথমটা দিয়ে শুরু
lowest = marks[0]
high_sub = subjects[0]
low_sub = subjects[0]

for i in range(5):
    print(f"{subjects[i]}: {marks[i]}")
    total = total + marks[i]

    if marks[i] > highest:
        highest = marks[i]
        high_sub = subjects[i]
    if marks[i] < lowest:
        lowest = marks[i]
        low_sub = subjects[i]

average = total / 5

print("---------------")
print(f"Total Marks: {total}/500")
print(f"Average: {average}%")
print(f"Highest: {high_sub} = {highest} 🔥")
print(f"Lowest: {low_sub} = {lowest}")

if average >= 90:
    print("Grade: A+ 👑 Loop Queen")
elif average >= 80:
    print("Grade: A ⭐ Game Dev")
else:
    print("Grade: B 💚 Keep Grinding")