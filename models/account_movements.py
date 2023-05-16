from models.base_model import BaseModel


class AccountMovements(BaseModel):

    def __init__(self, action, balance, date, amount) -> None:
        super().__init__()
        self.action = action
        self.date = date
        self.balance = balance
        self.amount = amount
        self.dbName = 'AccountMovements'
        pass

    def save_data(self):
        self.data_service.save_data(
            [self.action, self.balance, self.date, self.amount], self.dbName)
        pass
