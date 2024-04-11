import csv

def print_csv_file(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            linenum=1
            for row in csvreader:
                print("line - ", linenum)
                print(type(row))
                print(row)
                print(', '.join(row))
                linenum = linenum+1
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading the file: {e}")

def main():
    csv_file_path = 'print_csv.csv'
    print_csv_file(csv_file_path)

if __name__ == '__main__':
    main()
