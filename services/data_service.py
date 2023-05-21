import pandas
import csv
import os

class DataService():
    
    def __init__(self) -> None:
        pass
    
    def get_data(self,db_name):
        file = open(f"data/{db_name}.csv", "r")
        data = list(csv.reader(file, delimiter=","))
        file.close()
        return data

    def save_data(self, data, db_name):
        with open(f'data/{db_name}.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(data)
                
