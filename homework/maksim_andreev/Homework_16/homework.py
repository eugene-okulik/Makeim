import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv(override=True)


db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor()

with open('g:/Projects/Makeim/homework/eugene_okulik/Lesson_16/hw_data/data.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for line in csv_reader:
        query = f"SELECT * FROM students WHERE name = '{line['name']}' AND second_name = '{line['second_name']}'"
        cursor.execute(query)
        result = cursor.fetchone()
        if not result:
            print(f"Missing student: name: {line['name']}, second name: {line['second_name']}, "
                  f"group title: {line['group_title']}, book title: {line['book_title']}, subject title: "
                  f"{line['subject_title']}, lesson title: {line['lesson_title']}, mark value: {line['mark_value']}")
        else:
            print(f"Student found: name: {line['name']}, second name: {line['second_name']}, "
                  f"group title: {line['group_title']}, book title: {line['book_title']}, subject title: "
                  f"{line['subject_title']}, lesson title: {line['lesson_title']}, mark value: {line['mark_value']}")

cursor.close()
db.close()
