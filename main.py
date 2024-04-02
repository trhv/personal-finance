# from services.bank_service import BankService
from services.whatsup_service import WhatsupService
import json

# bank = BankService()
# bank.connect()
# bank.scrap()

# Open the JSON file
with open('fake_data.json', 'r') as file:
    # Load the JSON data
    data = json.load(file)

whatsUp = WhatsupService()
whatsUp.send(data)