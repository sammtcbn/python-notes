# example to remove row 3
import csv

def main():
    csv_file_path = 'row_del.csv'

    with open(csv_file_path, 'r') as infile, open('row_del_modified.csv', 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            writer.writerow(row[:2] + row[3:])


if __name__ == '__main__':
    main()
