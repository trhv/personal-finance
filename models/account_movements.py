from models.base_model import BaseModel


class AccountMovements(BaseModel):

    def __init__(self) -> None:
        super().__init__()
        self.dbName = 'AccountMovements'
        pass

    def save_data(self, action,balance,date,amount):
        self.data_service.save_data(
            [action, balance, date, amount], self.dbName)
        pass
