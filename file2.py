
    
  def save_student(name, total, avg):
    with open("class_result.txt", "a") as file:
        file.write(f"Name: {name} | Total: {total}/500 | Avg: {avg}%\n")
    print("✅ Data Save হয়ে গেল!")

def show_all_results():
    try:
        with open("class_result.txt", "r") as file:
            print("\n📄 সব Student এর Result 📄")
            print(file.read())
    except:
        print("❌ File এখনো বানানো হয়নি!")

def search_student():  # 👈 while এর উপরে, বাইরে
    search_name = input("কোন Student খুঁজবে? ")
    found = False  # 👈 Capital F
    try:
        with open("class_result.txt", "r") as file:
            for line in file:
                if search_name.lower() in line.lower():
                    print("✅ পাওয়া গেছে:", line.strip())
                    found = True
        if not found:
            print("❌ এই নামে কেউ নাই Database এ!")
    except:
        print("❌ File এখনো বানানো হয়নি। আগে Save করো!")

while True:  # 👈 সব menu এর ভিতরে থাকবে
    print("\n1. New Student Add করো")
    print("2. সব Result দেখো") 
    print("3. Student Search করো")  # 👈 Add কর
    print("4. Exit")  # 👈 Add কর
    choice = input("Option বাছো: ")
    
    if choice == "1":
        name = input("Name: ")
        total = int(input("Total Marks: "))
        avg = float(input("Average: "))
        save_student(name, total, avg)
    
    elif choice == "2":
        show_all_results()
    
    elif choice == "3":  # 👈 এটা Add কর
        search_student()
    
    elif choice == "4":  # 👈 এটা Add কর
        print("👋 Database বন্ধ হলো। Data Safe আছে!")
        break
    
    else:
        print("❌ 1, 2, 3 বা 4 চাপো!")