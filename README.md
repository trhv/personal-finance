# personal-finance

python3 -m pip freeze > requirements.txt
python3 -m pip install -r requirements.txt

create folder data and inside 3 files:
data/CreditCard 
data/AccountMovements 
data/AccountBalance

``` bash
mkdir data 
touch data/CreditCard.csv 
echo 'tags, businessName, date, numPayments,currentPayment, amount, owner' > data/CreditCard.csv

touch data/AccountMovements.csv 
echo 'action, balance, date, amount' > data/AccountMovements.csv

touch data/AccountBalance.csv
echo 'date, accountBalance' > data/AccountBalance.csv

```