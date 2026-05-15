# লাবনীর প্রথম File Handler 📄👑
# Data কে Permanently Save করা

# File এ লেখা = write mode "w"
def save_result(name, total, avg):
    file = open("result.txt", "w")  # "w" = write, নতুন file বানাবে
    file.write("🎓 STUDENT RESULT 🎓\n")
    file.write("=" * 25 + "\n")
    file.write(f"Name: {name}\n")
    file.write(f"Total: {total}/500\n")
    file.write(f"Average: {avg}%\n")

    if avg >= 90:
        grade = "A+ 👑 Class Topper"
    elif avg >= 80:
        grade = "A ⭐ Game Dev"
    elif avg >= 60:
        grade = "B 💚 Good"
    else:
        grade = "C 😅 Keep Grinding"

    file.write(f"Grade: {grade}\n")
    file.write("=" * 25 + "\n")
    file.close() # File বন্ধ করা Must
    print("✅ result.txt File এ Save হয়ে গেছে!")

# File থেকে পড়া = read mode "r"
def read_result():
    print("\n📄 File থেকে পড়ছি 📄")
    file = open("result.txt", "r")  # "r" = read
    data = file.read()  # সব Data একসাথে পড়ো
    file.close()
    print(data)

# Main Program 👇
print("📄 RESULT SAVER v1.0 📄")
name = input("Student এর নাম: ")
total = int(input("Total Marks: "))
avg = float(input("Average: "))

save_result(name, total, avg)  # File এ Save করো
read_result()                 # File থেকে পড়ে দেখাও

print("\n[Program finished] 🎉")