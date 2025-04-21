import numpy as np
import csv

def fail_and_pass_calc(array):
    exam1_pass_count = 0
    exam1_fail_count = 0
    exam2_pass_count = 0
    exam2_fail_count = 0
    exam3_pass_count = 0
    exam3_fail_count = 0

    # exam 1
    for i in array:
        if i[0] >= 60:
            exam1_pass_count += 1
        elif i[0] < 60:
            exam1_fail_count += 1

    print(f'Exam 1 Pass/Fail:'
          f'\n{exam1_pass_count} passed'
          f'\n{exam1_fail_count} failed')

    # exam 2
    for i in array:
        if i[1] >= 60:
            exam2_pass_count += 1
        elif i[1] < 60:
            exam2_fail_count += 1

    print(f'Exam 2 Pass/Fail:'
          f'\n{exam2_pass_count} passed'
          f'\n{exam2_fail_count} failed')

    # exam 3
    for i in array:
        if i[2] >= 60:
            exam3_pass_count += 1
        elif i[2] < 60:
            exam3_fail_count += 1

    print(f'Exam 3 Pass/Fail:'
          f'\n{exam3_pass_count} passed'
          f'\n{exam3_fail_count} failed')

    # pass percentage
    pass_count = sum([exam1_pass_count, exam2_pass_count, exam3_pass_count])
    pass_percent = 100*(pass_count / np.size(array))

    print(f'{pass_percent:.2f}% passing grades across all exams')


def main():
    with open('grades.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')

        grades_list = list(csv_reader)

        # removing names from list
        for item in grades_list:
            del item[0:2]


        array = np.array(grades_list)

        exam_grades = array.astype(np.float32)


    print(exam_grades)

    # need: mean, median, standard deviation, min, max
    print('First are the stats for each exam')

    mean_grades = np.mean(exam_grades, axis = 0)
    print(f'Means:'
          f'\nExam 1: {mean_grades[0]:.2f}%'
          f'\nExam 2: {mean_grades[1]:.2f}%'
          f'\nExam 3: {mean_grades[2]:.2f}%\n')

    median_grades = np.median(exam_grades, axis = 0)
    print(f'Medians:'
          f'\nExam 1: {median_grades[0]:.2f}%'
          f'\nExam 2: {median_grades[1]:.2f}%'
          f'\nExam 3: {median_grades[2]:.2f}%\n')

    stdev_grades = np.std(exam_grades, axis = 0)
    print(
        f'Standard Deviation:'
        f'\nExam 1: {stdev_grades[0]:.2f}%'
        f'\nExam 2: {stdev_grades[1]:.2f}%'
        f'\nExam 3: {stdev_grades[2]:.2f}%\n')

    min_grades = np.min(exam_grades, axis=0)
    print(
        f'Minimums:'
        f'\nExam 1: {min_grades[0]:.2f}%'
        f'\nExam 2: {min_grades[1]:.2f}%'
        f'\nExam 3: {min_grades[2]:.2f}%\n')

    max_grades = np.max(exam_grades, axis=0)
    print(
        f'Maximums:'
        f'\nExam 1: {max_grades[0]:.2f}%'
        f'\nExam 2: {max_grades[1]:.2f}%'
        f'\nExam 3: {max_grades[2]:.2f}%\n')

    print('Now the stats for all exams\n')
    mean_grade = np.mean(exam_grades)
    print(f'Mean: {mean_grade:.2f}%')

    mean_grade = np.median(exam_grades)
    print(f'Median: {mean_grade:.2f}%')

    mean_grade = np.std(exam_grades)
    print(f'Standard Deviation: {mean_grade:.2f}%')

    mean_grade = np.min(exam_grades)
    print(f'Mininum: {mean_grade:.2f}%')

    mean_grade = np.max(exam_grades)
    print(f'Maximum: {mean_grade:.2f}%\n\n')

    fail_and_pass_calc(exam_grades)

main()
