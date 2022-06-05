#!/usr/bin/env python3

import sys
import datetime
import os


my_days = 0

"""
create yaml folder structure
folder structure
make sure that if duplicate is found it does not delete any files within the folder.
- year
    -event
        - date(s)
            - camera(s)
                - photo
                    - raw
                    - full_size
                    - final
                    - social
                - video
            - microphone
                - phone

"""

def create_camera_folder(my_path,camera_name):
    os.popen(f'mkdir -p {my_path}/camera/{camera_name}/photo/raw')
    os.popen(f'mkdir -p {my_path}/camera/{camera_name}/photo/full_size')
    os.popen(f'mkdir -p {my_path}/camera/{camera_name}/photo/final')
    os.popen(f'mkdir -p {my_path}/camera/{camera_name}/photo/social')
    os.popen(f'mkdir -p {my_path}/camera/{camera_name}/video')


def create_folders(date,event):
    token_date = date.split('-')
    year = int(token_date[0])
    month = int(token_date[1])
    day = int(token_date[2])

    temp_date  = datetime.datetime(year, month, day) + datetime.timedelta(days = 0)
    the_date = temp_date.strftime("%Y-%m-%d")

    base_path = f'{year}/{event}/{the_date}'
    create_camera_folder(base_path,'a7iii')
    create_microphone_folder(base_path,'phone')

    for x in range(1,my_days):
        
        temp_date  = datetime.datetime(year, month, day) + datetime.timedelta(days = x)
        the_date = temp_date.strftime("%Y-%m-%d")

        base_path = f'{year}/{event}/{the_date}'
        create_camera_folder(base_path,'a7iii')
        create_microphone_folder(base_path,'phone')
    
    
def create_microphone_folder(my_path,microphone):
    os.popen(f'mkdir -p {my_path}/audio/{microphone}')


def validate(date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
        except ValueError:
            # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
            print('Date must be in YYYY-05-29')
            exit()


# check that there is at least an date, and event

if len(sys.argv) == 3:
    # this means we have date and event
    my_date = sys.argv[1]
    my_event = sys.argv[2]
elif len(sys.argv) == 4:
    # this means we have date + days and event
    my_date = sys.argv[1]
    my_days = int(sys.argv[2])
    my_event = sys.argv[3]

# check that date is the correct format



validate(my_date)

print(f'Setting {my_date} and {my_days} extra days')
create_folders(my_date,my_event)


