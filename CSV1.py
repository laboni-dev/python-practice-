print("📊 CSV Converter চালু হলো!")

try:
    with open("class_result.txt", "r") as txt_file:
        lines = txt_file.readlines()

    with open("result.csv", "w") as csv_file:
        csv_file.write("Name,Total,Average\n")

        for line in lines:
            data = line.split() # Space দিয়ে ভাগ কর
            if len(data) == 6: # নাম + 5টা নম্বর
                name = data[0]
                marks = [int(x) for x in data[1:6]]
                total = sum(marks)
                average = total / 5
                csv_file.write(f"{name},{total},{average}\n")

    print("✅ result.csv Save হয়ে গেছে!")

except FileNotFoundError:
    print("❌ class_result.txt পাওয়া যায়নি!") 