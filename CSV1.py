print("📊 CSV Converter চালু হলো!")

# Step 1: txt file পড়া
try:
    with open("class_result.txt", "r") as txt_file:
        lines = txt_file.readlines()

    # Step 2: csv file বানানো
    with open("result.csv", "w") as csv_file:
        # Header লিখি - Excel এ Column Name হবে
  csv_file.write("Name,Total,Average\n") 

        # Step 3: প্রতি Line Convert করা
        for line in lines:
            # "Name: laboni | Total: 236/500 | Avg: 90.3%"
            # থেকে Data বের করবো

            # Split by |
            parts = line.split("|")

            # Name বের করো: "Name: laboni " → "laboni"
            name = parts[0].replace("Name:", "").strip()

            # Total বের করো: " Total: 236/500 " → "236"
            total_part = parts[1].replace("Total:", "").strip()
            total = total_part.split("/")[0] # 236/500 থেকে 236

            # Avg বের করো: " Avg: 90.3%" → "90.3"
            avg = parts[2].replace("Avg:", "").replace("%", "").strip()

            # CSV তে লিখি: laboni,236,90.3
            csv_file.write(f"{name},{total},{avg}\n")

    print("✅ result.csv বানানো শেষ! Excel এ Open করো")

except:
    print("❌ class_result.txt পাওয়া যায়নি। আগে Day 7 এর Data বানা!")