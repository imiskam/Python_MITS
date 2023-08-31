import csv

# read csv
with open("diski.csv", encoding="utf-8") as file_r:
    file_reader = csv.reader(file_r)
    data_r = list(file_reader)
    print(data_r)
    for row in data_r:
        str_ = "Строка #" + str(file_reader.line_num) + " "
        for value in row:
            str_ = str_ + value + " "
        print(str_)

# write csv
with open("diski.csv", "a", encoding="utf-8", newline="") as file_w:
    file_writer = csv.writer(file_w)
    data_w = [["New User", "test@email.com", "150", "5.4 MB", "10.0 GB"], ["New User 2", "test2@email.com", "200", "50 MB", "10.0 GB"]]
    for row in data_w:
        file_writer.writerow(row)
