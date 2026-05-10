a = int(input("প্রথম সংখ্যা: "))
b = int(input("দ্বিতীয় সংখ্যা: "))
c = int(input("তৃতীয় সংখ্যা: "))

if a >= b and a >= c:
    print("বড় সংখ্যা:", a)
elif b >= a and b >= c:
    print("বড় সংখ্যা:", b)
else:
    print("বড় সংখ্যা:", c)