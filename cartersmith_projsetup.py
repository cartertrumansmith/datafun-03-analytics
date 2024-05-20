"""Project 2 Setup, Carter Smith
This module provides functions for creating a series of project folders. 
"""

#import dependencies
import pathlib
import math
import statistics
import time
import cartersmith_utils

#create folders for a given range
def create_folders_for_range(start, end):
    for i in range(start, end):
        pathlib.Path(f"{i}").mkdir(exist_ok=True)

#create folders from a list of folder names
def create_folders_from_list(folder_list):
    for folder in folder_list:
        pathlib.Path(folder).mkdir(exist_ok=True)

#create folders from a list of folder names with prefix 'data'
def create_prefixed_folders(folder_list, prefix):
    for folder in folder_list:
        pathlib.Path(f"{prefix}-{folder}").mkdir(exist_ok=True)

#create a folder every 5 seconds for the duration given
def create_folders_periodically(duration,period):
    start_time = time.time()
    while(time.time()-start_time < duration): #continue running while the time elapsed from start is less than the given duration
        current_time = time.time()-start_time
        pathlib.Path(f"Folder created at {round(current_time)} seconds").mkdir(exist_ok=True)
        time.sleep(period) #wait specified amount of seconds before beginning next iteration

# Create a path object
project_path = pathlib.Path.cwd()

# Define the new sub folder path
data_path = project_path.joinpath('data')

# Create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

def create_project_directory(dir_name: str):
    #creates a project sub-directory
    pathlib.Path(dir_name).mkdir(exist_ok=True)

def main():
    #print byline from imported module
    print(f"Byline: {cartersmith_utils.byline}")
    
    #create a folder for each number in a range 
    create_folders_for_range(start=2020,end=2024)
    
    #create a folder for each string in a list
    folder_names = ["Kansas City","Omaha","Chicago", "St Louis"]
    create_folders_from_list(folder_names)
    
    #create a folder for each string in a list with a specified prefix
    create_prefixed_folders(folder_names,prefix="Departures")
    
    
    #create a folder every 5 seconds for the specified duration
    create_folders_periodically(duration=15,period=5)

if __name__ == "__main__":
    main()