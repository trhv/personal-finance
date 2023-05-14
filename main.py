from services.bankService import BankService
from services.whatsupService import WhatsupService

bank = BankService()
bank.connect()
bank.scrap()

whatsUp = WhatsupService()
whatsUp.send()