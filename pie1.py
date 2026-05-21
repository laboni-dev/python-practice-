import pandas as pd
import matplotlib.pyplot as plt

# CSV পড়া
df = pd.read_csv('/storage/emulated/0/result.csv')

# Data বের করা
names = df['Name']
marks = df['Total']

# Pie Chart বানানো
plt.figure(figsize=(8, 8))
plt.pie(marks, labels=names, autopct='%1.1f%%', startangle=90)
plt.title('Laboni Er Marks Pie Chart 🥧')
plt.axis('equal')  # গোল করার জন্য

# Save করা
plt.savefig('/storage/emulated/0/pie.png')
print("Pie Chart Banano Complete ✅")
print("File Manager e pie.png check kor 💚")