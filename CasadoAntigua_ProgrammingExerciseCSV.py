import csv

def student_info_input():
    # initialize list to write to csv with header
    rows_list = []

    # decides how many times the loop is run, loop is for input validation
    while True:
        row_num = input('How many students will you enter? ')

        try:
            row_num = int(row_num)
        except ValueError:
            print('Error: Invalid Input')
            continue
        else:
            break

    # loop to input all the info for each student
    for i in range(row_num):

        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")

        while True:
            exam_1_grade = input("Enter student's grade on exam 1: ")

            try:
                exam_1_grade = int(exam_1_grade)
            except ValueError:
                print('Error: Invalid input')
                continue
            else:
                break

        while True:
            exam_2_grade = input("Enter student's grade on exam 2: ")
            try:
                exam_2_grade = int(exam_2_grade)
            except ValueError:
                print('Error: Invalid input')
                continue
            else:
                break

        while True:
            exam_3_grade = input("Enter student's grade on exam 3: ")
            try:
                exam_3_grade = int(exam_3_grade)
            except ValueError:
                print('Error: Invalid input')
                continue
            else:
                break



        # store the info to write to file later
        row = [first_name, last_name, exam_1_grade, exam_2_grade, exam_3_grade]
        rows_list.append(row)

    with open('grades.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows_list)


def student_info_read():

    with open('grades.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # print header
            if line_count == 0:
                print('%-12s %-12s %-8s %-8s %-8s' % ('First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'))
                print('-'*12, '-'*12, '-'*8, '-'*8, '-'*8)
                line_count += 1 # stops printing header
            print('%-12s %-12s %-8s %-8s %-8s' % (row[0], row[1], row[2], row[3], row[4]))
            line_count += 1


def main():

    # loop to ensure that the choice is a valid input
    while True:
        choice = input('Would you like to input student data or read it? (1 or 2) ')

        #if choice is neither valid option continue the loop
        if choice != '1' and choice != '2':
            print('Error: Invalid Input')
            continue
        else:
            break

    if choice == '1':
        student_info_input()
    elif choice == '2':
        student_info_read()



main()