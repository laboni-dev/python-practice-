import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv

# CSV থেকে Data পড়ে Grade বানানো
grades = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

with open('/storage/emulated/0/marks.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # Header Skip
    for row in reader:
        marks = int(row[1])
        if marks >= 90:
            grades['A'] += 1
        elif marks >= 80:
            grades['B'] += 1
        elif marks >= 70:
            grades['C'] += 1
        else:
            grades['D'] += 1

# Pie Chart বানানো
labels = grades.keys()
sizes = grades.values()
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99'] # A=Red, B=Blue, C=Green, D=Orange

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90,
        explode=(0.05, 0, 0, 0)) # A Grade কে একটু বের করে দে

plt.title('Day 12: Grade Distribution Pie Chart', fontsize=16)
plt.axis('equal') # Circle বানানোর জন্য

plt.savefig('/storage/emulated/0/marks_pie.png')
print("Level 3 Complete: Pie Chart Saved Boss ✅")
print(f"Grade Count: {grades}")