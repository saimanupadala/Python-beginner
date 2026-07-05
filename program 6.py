marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

total = sum(marks)
average = total / n

print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
else:
    print("Grade: D")
