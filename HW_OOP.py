class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   
 
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _av_grade(self):
        grades_list = []
        for grade in self.grades.values():
            grades_list.extend(grade)
            av_grade_res = round(sum(grades_list)/len(grades_list), 1)
        return av_grade_res

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self._av_grade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Не студент'
        return self._av_grade() < other._av_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades = {}

    def _av_grade(self):
        grades_list = []
        for grade in self.grades.values():
            grades_list.extend(grade)
            av_grade_res = round(sum(grades_list)/len(grades_list), 1)
        return av_grade_res

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self._av_grade()}')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Не лектор'
        return self._av_grade() < other._av_grade()


class Reviewer(Mentor):
    def rate_hw_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res_reviewer

 
student_1 = Student('Ruoy', 'Eman', 'man')
student_1.courses_in_progress += ['Python', 'OOP', 'Java']
student_1.finished_courses += ['C#']

student_2 = Student('Pam', 'Beasley', 'woman')
student_2.courses_in_progress += ['Python', 'Java']


reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python', 'OOP', 'Java']

reviewer_2 = Reviewer('Any', 'One')
reviewer_2.courses_attached += ['Java']


lecturer_1 = Lecturer('Michael', 'Scott')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Dwight', 'Schrute')
lecturer_2.courses_attached += ['OOP', 'Java', 'Python']
 
reviewer_1.rate_hw_student(student_1, 'Python', 10)
reviewer_1.rate_hw_student(student_1, 'Python', 7)
reviewer_1.rate_hw_student(student_1, 'Python', 3)
reviewer_1.rate_hw_student(student_1, 'OOP', 3)
reviewer_1.rate_hw_student(student_1, 'OOP', 8)
reviewer_1.rate_hw_student(student_1, 'OOP', 10)
reviewer_1.rate_hw_student(student_2, 'Python', 10)
reviewer_1.rate_hw_student(student_2, 'Python', 10)
reviewer_1.rate_hw_student(student_2, 'Python', 10)
reviewer_2.rate_hw_student(student_2, 'Java', 9)
reviewer_2.rate_hw_student(student_2, 'Java', 10)
reviewer_2.rate_hw_student(student_2, 'Java', 9)

student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_1, 'Python', 7)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 5)
student_1.rate_lecturer(lecturer_2, 'OOP', 10)
student_1.rate_lecturer(lecturer_2, 'OOP', 7)
student_1.rate_lecturer(lecturer_2, 'OOP', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 6)
student_2.rate_lecturer(lecturer_2, 'Python', 5)
student_2.rate_lecturer(lecturer_2, 'Python', 1)
student_2.rate_lecturer(lecturer_2, 'Python', 5)
student_2.rate_lecturer(lecturer_2, 'Java', 10)
student_2.rate_lecturer(lecturer_2, 'Java', 10)
student_2.rate_lecturer(lecturer_2, 'Java', 10)


# print(student_1.grades)
# print(student_2.grades)
# print(lecturer_1.grades)
# print(lecturer_2.grades)

# для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса 
# (в качестве аргументов принимаем список студентов и название курса):

students_list = [student_1, student_2]


def av_grade_hw_course(students_list, course):
    st_list = []
    sum_grades = 0
    for student in students_list:
        if course in student.grades.keys():
            st_list.append(student)
            sum_grades += sum(student.grades.get(course))/len(student.grades.get(course))
    res = round(sum_grades/len(st_list), 1)
    print(res)

av_grade_hw_course(students_list, 'Java')

# для подсчета средней оценки за лекции всех лекторов в рамках курса 
# (в качестве аргумента принимаем список лекторов и название курса):

lectors_list = [lecturer_1, lecturer_2]

def av_grade_lect_course(lectors_list, course):
    lec_list = []
    sum_grades = 0
    for lecturer in lectors_list:
        if course in lecturer.grades.keys():
            lec_list.append(lecturer)
            sum_grades += sum(lecturer.grades.get(course))/len(lecturer.grades.get(course))
    res = round(sum_grades/len(lec_list), 1)
    print(res)

av_grade_lect_course(lectors_list, 'Java')