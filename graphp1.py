import matplotlib.pyplot as plt
import csv

# Step 1: CSV থেকে Data পড়বি
names = []
marks = []

with open('result.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # Header skip করলাম
    for row in reader:
        names.append(row[0])
        marks.append(int(row[1]))

# Step 2: Graph বানাবি
plt.figure(figsize=(10, 6))
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
bars = plt.bar(names, marks, color=colors)

# Step 3: সুন্দর করবি
plt.title('Laboni Er Result Dashboard 📊', fontsize=16, fontweight='bold')
plt.xlabel('Students', fontsize=12)
plt.ylabel('Total Marks', fontsize=12)
plt.ylim(0, 500)

# Bar এর উপরে Marks লিখবি
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}', ha='center', va='bottom', fontsize=10)

# Step 4: Save করবি
plt.tight_layout()
plt.savefig('result.png', dpi=300)
print("Graph বানানো Complete! ✅")
print("Gallery তে result.png Check কর 📸")