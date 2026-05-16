# লাবনীর Class Topper v3.0 - Database Edition 📄💳👑
# Append Mode দিয়ে Permanent Storage

print("💳 CLASS TOPPER v3.0 - DATABASE 💳")
print("=" * 35)

def save_student(name, total, avg):
    # "a" = Append Mode। পুরানো Data Delete হবে না
    with open("class_result.txt", "a") as file:
        file.write(f"Name: {name} | Total: {total}/500 | Avg: {avg}%\n")
    print(f"✅ {name} এর Data Save হয়ে গেল!")

def show_all_results():
    print("\n📄 সব Student এর Result 📄")
    print("=" * 35)
    try:
        with open("class_result.txt", "r") as file:
            data = file.read()
            if data == "":
                print("❌ এখনো কেউ Save হয়নি!")
            else:
                print(data)
    except:
        print("❌ File এখনো বানানো হয়নি। আগে Save করো!")

# Main Program 👇
while True:
    print("\n1. New Student Add করো")
    print("2. সব Result দেখো") 
    print("3. Exit")
    choice = input("Option বাছো: ")

    if choice == "1":
        name = input("Student নাম: ")
        total = int(input("Total Marks: "))
        avg = float(input("Average: "))
        save_student(name, total, avg)
        
    elif choice == "2":
        show_all_results()
        
    elif choice == "3":
        print("👋 Database বন্ধ হলো। Data Safe আছে!")
        break
        
    else:
        print("❌ 1, 2 বা 3 চাপো!")