# Entering the total classes held by the college/school
total_classes = int(input("Enter the total number of classes held this year: "))

# Entering the classes attended by the student
classes_attended = int(input("Enter the number of classes attended by the student: "))

# Calculating the attendace percentage of the student
attendance_percentage = ((classes_attended/total_classes) * 100)

if(attendance_percentage > 75):
    print("Student is eligible to give the exam.")
else:
    print("Student is not eligible to give the exam")

    