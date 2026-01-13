'''
student1_name = "Katelyn"
student1_grade = "1.0"
student1_subject = ["Calculus, Chemistry"]

student2_name = "Andrei"
student2_grade = "1.5"
student2_subject = ["Algebra, Chemistry"]

student3_name = "Koby"
student3_grade = "2.5"
student3_subject = ["Calculus, Geometry"]


def print_student_info_function(name, grade, subject):
    print(f"{name} grade: {grade}, course: {subject}")

if __name__ == "__main__":
      print_student_info_function(student1_name, student1_grade, student1_subject)
      print_student_info_function(student2_name, student2_grade, student2_subject)
      print_student_info_function(student3_name, student3_grade, student3_subject)
'''

class Student(object):
    DEFAULT_SUBJECT = ["BASIC ELECTRONICS", "BASIC PROGRAMMING"]
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def print_student_info_method(self):
        print(f"{self.name} grade: {self.grade}, course: {self.subject}")

    @classmethod
    def create_student(cls, name, grade):
        print(f"{name} grade: {grade}, subject: {cls.DEFAULT_SUBJECT}")

    @staticmethod
    def is_grade_passing(grade):
        return grade <= 3.0

if __name__ == "__main__":
    student1 = Student("Ken", 3.5, ["Physics", "Chemistry"])
    student1.print_student_info_method()
    if Student.is_grade_passing(student1.grade):
        print("Pass")
    else:
        print("Fail")

    student2 = Student.create_student("Drei", 1.0,)
    if Student.is_grade_passing(student1.grade):
        print("Pass")
    else:
        print("Fail")
