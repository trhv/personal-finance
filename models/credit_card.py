from models.base_model import BaseModel


class CreditCard(BaseModel):

    def __init__(self, tags, businessName, date,
                 numPayments, currentPayment, amount, owner) -> None:
        super().__init__()
        self.tags = tags
        self.businessName = businessName
        self.date = date
        self.numPayments = numPayments
        self.currentPayment = currentPayment
        self.amount = amount
        self.owner = owner
        self.dbName = 'CreditCard'
        pass

    def save_data(self):
        self.data_service.save_data(
            [self.tags, self.businessName,
                self.date, self.numPayments, self.currentPayment,
             self.amount, self.owner], self.dbName)
        print('saving CreditCard')
        pass
