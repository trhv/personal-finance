# import pywhatkit
# from models.account_balance import AccountBalance
# from models.account_movements import AccountMovements
# from models.credit_card import CreditCard
import datetime


class WhatsupService():

    def __init__(self) -> None:
        # self.account_balance = AccountBalance()
        # self.account_movements = AccountMovements()
        # self.credit_card = CreditCard()
        pass

    # def _get_credit_card_data(self):
    #     pass

    # def _get_account_balance_data(self):
    #     balance = self.account_balance.get_data()
    #     return f"Account status as of:{datetime.today().strftime('%Y-%m-%d')}, is: {balance}"

    # def _get_account_movements_data(self):
    #     pass

    # def _prepare_data(self):
    #     # account_movements_data = self.get_account_movements_data()
    #     account_balance_data = self._get_account_balance_data()
    #     # credit_card_data = self.get_credit_card_data()
    #     return f'{account_balance_data}'
    #     pass

    def _parse_account_movements(self,data):
        res = ''
        for mov in data["account_movements"]:
            res +=f"\tDate: {mov["date"]}, Action: {mov["action"]}, Amount: {mov["amount"]}\n\n\t"
        msg = f"""
        Last Day Movements:
        {res}
        """
        return msg

    def _parse_account_balance(self,data):
        current_date = datetime.date.today()
        res = f"""
        Good Morning !!!
        Account state as of date: {current_date}
        \t{'-'+data["balance"]["amount"] if data["balance"]["in_debt"] else data["balance"]["amount"]}  
        """
        return res
    
    def _parse_card(self,card_movements):
        print(card_movements)
        res = ''
        for mov in card_movements:
            res +=f"\tDate: {mov["date"]}, business: {mov["business"]}, Amount: {mov["amount"]}\n\n\t"
        # msg = f"""
        # Last Day Movements:
        # {res}
        # """
        return res
    
    def _parse_credit_card(self,data):
        msg = ''
        ilona_card = self._parse_card(data["credit_cards"]["ilona"]["charges"])
        # arye_card = self._parse_card(data["credit_cards"]["arye"]["charges"])
        msg =f"""Credit Card Activities:
        \tIlona: 
        \t  Total: {data["credit_cards"]["ilona"]["total"]}
            {ilona_card}
        """
        return msg
    
    def _prepare_message(self,data):
        acc_balance = self._parse_account_balance(data)
        acc_movements = self._parse_account_movements(data)
        acc_credit_cards = self._parse_credit_card(data)
        msg= f"""
        {acc_balance} 
        {acc_movements}
        {acc_credit_cards}
        """
        return msg
    
    def send(self,data):
        msg = self._prepare_message(data)
        print(msg)
        # pywhatkit.sendwhatmsg('+972542465284', 'Message 666', 17, 45,15, True, 2)
