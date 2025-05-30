name = "Bro"
sub1 = 75
sub2 = 80
sub3 = 90

total = sub1 + sub2 + sub3
average = total / 3

if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "Fail"

print("\n--- Report Card ---")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)