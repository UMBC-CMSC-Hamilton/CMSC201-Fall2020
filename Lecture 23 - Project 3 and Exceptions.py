"""
    We're not going to do exceptions.

    Let's do a little bit of a csv/json tutorial.
"""

import csv


def csv_write_test():
    with open('test.csv', 'w', newline='') as test_csv_file:
        # open the file in write mode, stick it in the csv.writer constructor
        my_writer = csv.writer(test_csv_file)

        row = ["i have a comma, yes i do", 2, 3]
        for i in range(10):
            # write row is going to add its own newline
            # you gotta have no additional endlines
            my_writer.writerow(row)

    with open('test.csv', 'r') as read_csv_file:
        my_reader = csv.reader(read_csv_file)

        for line in my_reader:
            print(line)


def dictionary_csv_test():
    with open('dict_test.csv', 'w', newline='') as test_csv_file:
        header = ['Area Code', 'Phone Number', 'Connected Areas']
        my_writer = csv.DictWriter(test_csv_file, fieldnames=header)

        my_writer.writeheader()
        row = {'Area Code': 443, 'Phone Number': "210-2211", 'Connected Areas': [410, 310, 221]}
        for i in range(10):
            # write row is going to add its own newline
            # you gotta have no additional endlines
            my_writer.writerow(row)

    with open('dict_test.csv', 'r') as test_csv_read:
        my_reader = csv.DictReader(test_csv_read)
        print(my_reader.fieldnames)
        for line in my_reader:
            print(line['Phone Number'])


csv_write_test()
dictionary_csv_test()
