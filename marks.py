class Student:
    def __init__(self, name, rollno, m1, m2, m3, m4, m5):
        self.name = name
        self.rollno = rollno
        self.__marks = [m1, m2, m3, m4, m5]

    def total(self):
        return sum(self.__marks)

    def highest(self):
        return max(self.__marks)

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("Marks:", self.__marks)
        print("Total Marks:", self.total())
        print("Highest Subject Marks:", self.highest())
        print()


# Enter details of 3 students
s1 = Student("Rahul", 101, 80, 75, 90, 85, 95)
s2 = Student("Aman", 102, 88, 92, 85, 90, 89)
s3 = Student("Priya", 103, 95, 94, 91, 96, 98)

# Store all students
students = [s1, s2, s3]

# Display details of all students
for s in students:
    s.display()

# Find student with highest total marks
topper = max(students, key=lambda s: s.total())

print("Student with Highest Total Marks:")
print("Name:", topper.name)
print("Roll No:", topper.rollno)
print("Total Marks:", topper.total())
