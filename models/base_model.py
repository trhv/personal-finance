from services.data_service import DataService
from datetime import datetime

class BaseModel():
    
    def __init__(self) -> None:
        self.datetime = datetime
        self.data_service = DataService()
        pass
    
    def save_data(self):
        print('saving')
        pass