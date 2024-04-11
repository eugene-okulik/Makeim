import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    password='AVNS_tegPDkI5BlB2lW5eASC',
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    database='st-onl'
)

cursor = db.cursor()

# Добавление студента
student_name = 'Maksim'
student_second_name = 'Andreev'
group_title = 'andreev_group'
group_start_date = 'mart'
group_end_date = 'june'
group_query = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
cursor.execute(group_query, (group_title, group_start_date, group_end_date))
group_id = cursor.lastrowid
students_query = 'INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)'
cursor.execute(students_query, (student_name, student_second_name, group_id))
student_id = cursor.lastrowid


book_query = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
book_titles = ['Chrono_Book', 'Emotion_Book', 'Everything_Book']
for book_title in book_titles:
    cursor.execute(book_query, (book_title, student_id))

subject_query = 'INSERT INTO subjets (title) VALUES (%s)'
lessons_query = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
subject_titles = ['Chronoscope', 'Emotional_Int']
lesson_titles = ['Chrono_Planning', 'Chrono_Study', 'Control_Stress', 'Recognition_Emotions']
for subject_title in subject_titles:
    cursor.execute(subject_query, (subject_title,))
    subject_id = cursor.lastrowid
    for lesson_title in lesson_titles:
        cursor.execute(lessons_query, (lesson_title, subject_id))

marks_query = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
lesson_ids = [1, 2, 3, 4]
marks = [5, 4, 5, 5]
for lesson_id, mark in zip(lesson_ids, marks):
    cursor.execute(marks_query, (mark, lesson_id, student_id))

final_query = 'SELECT s.name, s.second_name, g.title AS group_title, b.title AS book_title, l.title AS lesson_title,'\
                    ' m.value AS mark FROM students s JOIN `groups` g ON s.group_id = g.id JOIN books b '\
                    'ON s.id = b.taken_by_student_id JOIN marks m ON s.id = m.student_id JOIN lessons l '\
                    'ON m.lesson_id = l.id JOIN subjets subj ON l.subject_id = subj.id WHERE s.id = %s'
cursor.execute(final_query, (student_id,))
result = cursor.fetchall()
for every_result in result:
    print(every_result)

db.commit()
db.close()
