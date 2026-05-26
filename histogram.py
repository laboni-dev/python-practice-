import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv

# CSV থেকে Marks পড়া
marks = []

with open('/storage/emulated/0/marks.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # Header Skip কর
    for row in reader:
        marks.append(int(row[1]))

# Histogram বানানো
plt.figure(figsize=(10, 6))
plt.hist(marks, bins=5, color='purple', edgecolor='black', alpha=0.7)

plt.title('20 Students Marks Distribution')
plt.xlabel('Marks Range')
plt.ylabel('Number of Students')
plt.grid(axis='y', alpha=0.3)

# Bins এর মানে: 65-75, 75-85, 85-95, 95-105 এই 5টা Range

plt.savefig('/storage/emulated/0/histogram.png')
print("Level 1 Complete: Histogram Saved Boss ✅")