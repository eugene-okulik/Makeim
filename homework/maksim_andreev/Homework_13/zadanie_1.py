from datetime import datetime, timedelta
import os

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data.txt')
hmwrk_path = os.path.dirname(os.path.dirname(base_path))
egn_filepath = os.path.join(hmwrk_path, 'eugene_okulik', 'hw_13', 'data.txt')


with open(egn_filepath) as hw_file:
    for line in hw_file:
        parts = line.split(' - ')

        date_str = parts[0].split('. ')[1].strip()
        date_format = '%Y-%m-%d %H:%M:%S.%f'

        date_time = datetime.strptime(date_str, date_format)
        if parts[0].startswith('1'):
            new_date = date_time + timedelta(weeks=1)
            print(f'The date {date_time} plus one week =  {new_date.strftime(date_format)}')
        if parts[0].startswith('2'):
            day_of_week = date_time.strftime('%A')
            print(f'Weekday of the date {date_time} - {day_of_week}')
        if parts[0].startswith('3'):
            today = datetime.now()
            diff = (today - date_time).days
            print(f'Passed {diff} days from {date_time}')
