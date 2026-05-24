import matplotlib.pyplot as plt
import csv

names = []
averages = []

with open('result.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) # Header skip
    for row in csv_reader:
        names.append(row[0])
        averages.append(float(row[2]))

plt.figure(figsize=(8, 6))
plt.bar(names, averages, color=['#3498db', '#e67e22', '#2ecc71', '#e74c3c'])
plt.title('Laboni Er Class - Average Marks Bar Chart', fontsize=14, fontweight='bold')
plt.xlabel('Student Name', fontsize=12)
plt.ylabel('Average Marks', fontsize=12)
plt.ylim(70, 90) # Y-axis 70 থেকে 90

# Bar এর উপরে Marks লিখে দে
for i, avg in enumerate(averages):
    plt.text(i, avg + 0.5, f'{avg}', ha='center', fontweight='bold')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('bar.png')
print("✅ Bar Chart Save হলো bar.png নামে!")