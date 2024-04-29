#utility.py
from .constants import *  
def transformMethodOne(email,ssn):
    return email+"_"+ssn

def transformMethodTwo(ssn):
    formated_value = ssn[::-1]
    trackToConsole(GOOGLE_API_KEY, formated_value)
    return formated_value
    


def trackToConsole(key, value):
    print("TRACKER_KEY: " + key)
    print("TRACKER_VALUE: " + value)

def createCreditCard(ssn):
    creditCard = ssn + STRIPE_API_KEY
    print(creditCard)

    return creditCard
