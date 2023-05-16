from models.base_model import BaseModel

class AccountBalance(BaseModel):
    
    def __init__(self, balance) -> None:
        super().__init__()
        self.balance = balance
        self.dbName = 'AccountBalance'
        pass
    
    def save_data(self):
        self.data_service.save_data([self.balance,self.datetime.today().strftime('%Y-%m-%d')],self.dbName)