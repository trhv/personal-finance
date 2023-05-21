from models.base_model import BaseModel

class AccountBalance(BaseModel):
    
    def __init__(self) -> None:
        super().__init__()
        self.dbName = 'AccountBalance'
        self.curr_date = self.datetime.today().strftime('%Y-%m-%d')
        pass
    
    def get_data(self):
        data = self.data_service.get_data(self.dbName)
        curr_balance = ''
        for balance in reversed(data):
            if self.curr_date == balance[0]:
                curr_balance = balance[1]
                break
        return curr_balance
    
    def save_data(self,balance):
        self.data_service.save_data([self.curr_date,balance],self.dbName)