# currency converter - a simple program to convert a given amount from one currency to another currency
# Talha Asghar
# 09-Sep-23


# USD to USD
#        PKR
#        GBP         
rates = {'USD': 1, 'PKR': 306, 'GBP': 0.8, 'JPY': 147.7, 'EUR': 0.93, 'BHD': 0.376, 'MYR': 4.67, 'INR': 83}

amount = int(input('Enter amount:'))
# we will assume that user will enter 3-digit ISO-4217 currency code
from_ = input('Enter original currency: ')
to = input('Enter target currency:')

# 45 PKR -> MYR
# 1 * usd = 306 * pkr .i.e. rates['pkr'] 
# 1 pkr = (1 * usd) / (rates['pkr'])

if from_ != 'USD':
    usds = (1 / rates[from_]) * amount 
    print(rates[to] * usds)
else:
    print(amount * rates[to])



