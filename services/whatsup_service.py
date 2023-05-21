import pywhatkit
from models.account_balance import AccountBalance
from models.account_movements import AccountMovements
from models.credit_card import CreditCard
from datetime import datetime


class WhatsupService():

    def __init__(self) -> None:
        self.account_balance = AccountBalance()
        # self.account_movements = AccountMovements()
        # self.credit_card = CreditCard()
        pass

    def _get_credit_card_data(self):
        pass

    def _get_account_balance_data(self):
        balance = self.account_balance.get_data()
        return f"Account status as of:{datetime.today().strftime('%Y-%m-%d')}, is: {balance}"

    def _get_account_movements_data(self):
        pass

    def _prepare_data(self):
        # account_movements_data = self.get_account_movements_data()
        account_balance_data = self._get_account_balance_data()
        # credit_card_data = self.get_credit_card_data()
        return f'{account_balance_data}'
        pass

    def send(self):
        msg = self._prepare_data()
        print(msg)
        # pywhatkit.sendwhatmsg('+972542465284', 'Message 666', 17, 45,15, True, 2)
