class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _calc_average_grade(self):
        grades_list = []
        for values in self.grades.values():
            grades_list += values
        average_grade = sum(grades_list) / len(grades_list)
        return round(average_grade, 1)

    def __str__(self):
        text = f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self._calc_average_grade()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return text

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self._calc_average_grade() < other._calc_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _calc_average_grade(self):
        grades_list = []
        for values in self.grades.values():
            grades_list += values
        average_grade = sum(grades_list) / len(grades_list)
        return round(average_grade, 1)

    def __str__(self):
        text = f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self._calc_average_grade()}'
        return text

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self._calc_average_grade() < other._calc_average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'
        return text


student_1 = Student('Ivan', 'Smirnov', 'male')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Git', 'Java']

student_2 = Student('Marina', 'Kuznecova', 'female')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Java']

lecturer_1 = Lecturer('Oleg', 'Voynov')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Elena', 'Krutickaya')
lecturer_2.courses_attached += ['Git']

reviewer_1 = Reviewer('Igor', 'Semenov')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Alexandr', 'Gromov')
reviewer_2.courses_attached += ['Git']

student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Python', 10)

student_2.rate_lecture(lecturer_1, 'Python', 10)
student_2.rate_lecture(lecturer_1, 'Python', 9)
student_2.rate_lecture(lecturer_1, 'Python', 9)

student_2.rate_lecture(lecturer_1, 'Git', 9)
student_2.rate_lecture(lecturer_1, 'Git', 10)
student_2.rate_lecture(lecturer_1, 'Git', 9)

student_2.rate_lecture(lecturer_2, 'Git', 10)
student_2.rate_lecture(lecturer_2, 'Git', 9)
student_2.rate_lecture(lecturer_2, 'Git', 9)
student_2.rate_lecture(lecturer_2, 'Git', 9)

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 10)

reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Git', 10)


students_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]


def calc_students_average_grade(students, course):
    grades_list = []
    for student in students:
        if course in student.grades:
            grades_list += student.grades[course]
    average_grade = sum(grades_list) / len(grades_list)
    return round(average_grade, 1)


def calc_lecturers_average_grade(lecturers, course):
    grades_list = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            grades_list += lecturer.grades[course]
    average_grade = sum(grades_list) / len(grades_list)
    return round(average_grade, 1)


print(student_1.grades)
print(student_1)
print()
print(student_2.grades)
print(student_2)
print()
print(lecturer_1.grades)
print(lecturer_1)
print()
print(lecturer_2.grades)
print(lecturer_2)
print()
print(reviewer_1)
print()
print(reviewer_2)
print()
print(student_1 > student_2)
print(lecturer_1 < lecturer_2)
print()
print(calc_students_average_grade(students_list, 'Python'))
print(calc_students_average_grade(students_list, 'Git'))
print()
print(calc_lecturers_average_grade(lecturer_list, 'Python'))
print(calc_lecturers_average_grade(lecturer_list, 'Git'))
