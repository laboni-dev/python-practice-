# লাবনীর Result Saver v1.1 📄👑
# Permission Error Fix সহ

def save_result(name, total, avg):
    try:
        # "with" use করলে file.close() লাগে না
        with open("result.txt", "w") as file:
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
        print("✅ result.txt File এ Save হয়ে গেছে!")

    except PermissionError:
        print("❌ Phone এ File বানাতে দিচ্ছে না।")
        print("💡 নিচের Result টা Copy করে রাখো:")
        print("=" * 25)
        print(f"Name: {name}")
        print(f"Total: {total}/500")
        print(f"Average: {avg}%")
        print("=" * 25)

def read_result():
    try:
        print("\n📄 File থেকে পড়ছি 📄")
        with open("result.txt", "r") as file:
            data = file.read()
        print(data)
    except:
        print("❌ File পাওয়া যায়নি। আগে Save করো।")

# Main Program 👇
print("📄 RESULT SAVER v1.1 📄")
name = input("Student এর নাম: ")
total = int(input("Total Marks: "))
avg = float(input("Average: "))

save_result(name, total, avg)
read_result()

print("\n[Program finished] 🎉")