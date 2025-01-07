
marks_1 = float(input("Enter marks for subject 1: "))
marks_2 = float(input("Enter marks for subject 2: "))
marks_3 = float(input("Enter marks for subject 3: "))


average = (marks_1 + marks_2 + marks_3) / 3


if average >= 90:
    print("Grade: A")
elif 80 <= average < 90:
    print("Grade: B")
elif 70 <= average < 80:
    print("Grade: C")
else:
    print("Grade: Fail")
