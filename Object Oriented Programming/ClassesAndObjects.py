student: {
    'name': "Mike",
    'grades': [70,88,90,99],
    'average': None
}

def average_grade(student):
    return sum(student['grades']) / len(student['grades'])

class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def example(self):
        print("Hello")

student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Jose', [50,60,99,100])

print(student_one.name)
student_one.example()
#Student.example()
print(student_two.name)