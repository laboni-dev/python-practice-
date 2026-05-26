import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv

# CSV থেকে Data পড়া
students = []
marks = []

with open('/storage/emulated/0/marks.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # Header Skip
    for row in reader:
        students.append(row[0]) # Student Name
        marks.append(int(row[1])) # Marks

# Scatter Plot বানানো
plt.figure(figsize=(12, 6))
plt.scatter(students, marks, color='blue', s=100, alpha=0.7, edgecolor='black')

plt.title('Day 12: Students vs Marks Scatter Plot', fontsize=14)
plt.xlabel('Student Names', fontsize=12)
plt.ylabel('Marks', fontsize=12)
plt.xticks(rotation=45) # নামগুলো ঘুরিয়ে দে যাতে Clear দেখা যায়
plt.grid(True, alpha=0.3)
plt.tight_layout() # Layout ঠিক করার জন্য

plt.savefig('/storage/emulated/0/scatter.png')
print("Level 2 Complete: Scatter Plot Saved Boss ✅")