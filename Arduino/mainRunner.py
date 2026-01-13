import newRunner

student1_name = "Nichole"
student1_grade = "2.0"
student1_subject = ["Calculus, Chemistry"]

newRunner.print_student_info_function(student1_name, student1_grade, student1_subject)

student1 = newRunner.Student("Nichole", 2.0, ["Calculus", "Chemistry"])
student1.print_student_info_method()
