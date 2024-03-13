import sqlite3

# Connect to or create an SQLite database
conn = sqlite3.connect('student.db')

# Create a cursor
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY,
                    student_name TEXT,
                    gender TEXT
                )''')

# Insert 10 records
students_data = [
    (1, 'John', 'Male'),
    (2, 'Emily', 'Female'),
    (3, 'Michael', 'Male'),
    (4, 'Sarah', 'Female'),
    (5, 'David', 'Male'),
    (6, 'Emma', 'Female'),
    (7, 'Daniel', 'Male'),
    (8, 'Olivia', 'Female'),
    (9, 'James', 'Male'),
    (10, 'Sophia', 'Female')
]

# Insert data into the table
cursor.executemany('''INSERT INTO students (student_id, student_name, gender)
                      VALUES (?, ?, ?)''', students_data)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Data has been successfully created and inserted into the SQLite database!")

