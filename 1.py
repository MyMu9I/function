def average_grade(a, b, c):
    return (a + b + c) / 3
def grade_message(average):
    if average >= 4.5:
        return "Отлично"
    if average >= 3.5:
        return "Хорошо"
    return "Нужно повторить материал"
avg = average_grade(5, 4, 5)
print(avg, grade_message(avg))
avg = average_grade(3, 4, 3)
print(avg, grade_message(avg))
