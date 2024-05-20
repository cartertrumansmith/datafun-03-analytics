'''
44608, Project 3, Carter Smith
'''

#import dependencies
import csv
import pathlib
import requests
import pandas as pd
import json
import os
import cartersmith_utils      
import cartersmith_projsetup 

#data acquisition
def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_txt_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_excel_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")

def fetch_and_write_csv_data(folder_name, filename,url):
    response = requests.get(url)
    if response.status_code == 200:
        write_csv_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch CSV data: {response.status_code}")

def fetch_and_write_json_data(folder_name, filename,url):
    response = requests.get(url)
    if response.status_code == 200:
        write_json_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch JSON data: {response.status_code}")

#write data
def write_txt_file(folder_name, filename, data):
    pathlib.Path(folder_name).mkdir(exist_ok=True)
    file_path = pathlib.Path(folder_name).joinpath(filename) # use pathlib to join paths
    with file_path.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")

def write_excel_file(folder_name, filename, data):
    pathlib.Path(folder_name).mkdir(exist_ok=True)
    file_path = pathlib.Path(folder_name).joinpath(filename) # use pathlib to join paths
    with open(file_path, 'wb') as file:
        file.write(data)
        print(f"Excel data saved to {file_path}")

def write_csv_file(folder_name, filename, data):
    pathlib.Path(folder_name).mkdir(exist_ok=True)
    file_path = pathlib.Path(folder_name).joinpath(filename) # use pathlib to join paths
    with open(file_path, 'wb') as file:
        file.write(data)
        print(f"CSV data saved to {file_path}")

def write_json_file(folder_name, filename, data):
    pathlib.Path(folder_name).mkdir(exist_ok=True)
    file_path = pathlib.Path(folder_name).joinpath(filename) # use pathlib to join paths
    with open(file_path, 'wb') as file:
        file.write(data)
        print(f"JSON data saved to {file_path}")

#process data/generate output
def process_txt_file(folder_name,input_txt,output_txt):
    path = pathlib.Path(folder_name).joinpath(input_txt) 
    txt = open(path, 'r', encoding='utf-8').read()
    word_count = 0
    for word in txt:
        word_count += 1
    print(word_count)
    file_path = pathlib.Path(folder_name).joinpath(output_txt)
    with file_path.open('w') as file:
        file.write(f"word count: {word_count}")
        print(f"Text data saved to {output_txt}")

def process_csv_file(folder_name,input,output):
    path = pathlib.Path(folder_name).joinpath(input) 
    input_csv = open(path, 'r', encoding='utf-8').read()
    rows = []
    with open(path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        #fields = next(csvreader)
        for row in csvreader:
            rows.append(row[0])
            #print(f"{row[0]}")
    print("Total no. of rows: %d" % (csvreader.line_num))
    file_path = pathlib.Path(folder_name).joinpath(output)
    with file_path.open('w') as file:
        file.write(f"row count: {csvreader.line_num}")
        for row in rows:
            file.write(f"{row}\n")
        print(f"Text data saved to {output}")

def process_excel_file(folder_name,input,output):
    path = pathlib.Path(folder_name).joinpath(input)
    
    #input_xls = open(path, 'r').read()
    df = pd.read_excel(path)
    descriptive = df.describe().to_string()
    out_path = pathlib.Path(folder_name).joinpath(output)
    with out_path.open('w') as file:
        file.write(f"Descriptive Statistics: \n{descriptive}")

def process_json_file(folder_name,input,output):
    path = pathlib.Path(folder_name).joinpath(input) 
    input_json = open(path, 'r', encoding='utf-8').read()
    data = json.loads(input_json)
    people = data['people']
    out_path = pathlib.Path(folder_name).joinpath(output)
    with out_path.open('w') as file:
        for person in people:
            file.write(f"Name: {person['name']}\n")
        

def main():
    #print('Hello, World!')

    txt_url = 'https://shakespeare.mit.edu/romeo_juliet/full.html'

    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv' 

    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls' 
    
    json_url = 'http://api.open-notify.org/astros.json'
    
    new_url = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt' #MIT seemed to be throwing errors

    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json' 

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls' 
    json_filename = 'data.json' 

    fetch_and_write_txt_data(txt_folder_name, txt_filename, new_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename,excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename,json_url)

    process_txt_file(txt_folder_name,'data.txt', 'results_txt.txt')
    process_csv_file(csv_folder_name,'data.csv', 'results_csv.txt')
    process_excel_file(excel_folder_name,'data.xls', 'results_xls.txt')
    process_json_file(json_folder_name,'data.json', 'results_json.txt')
    process_csv_file(csv_folder_name,'royals.csv','royals_results.txt')
    
    
    
    #print(requests.get(new_url))

if __name__ == "__main__":
    main()