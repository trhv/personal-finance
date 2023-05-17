import pandas
import csv
import os

class DataService():
    
    def __init__(self) -> None:
        pass
    
    def save_data(self, data, dbName):
        with open(f'data/{dbName}.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(data)
                
