# Multi Inheritence

class Card:
    def __init__(self):
        pass

    def doSomething(self):
        print("Card do something")

class ATMcard(Card):
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def doSomething(self):
        return "ATM Class"
    
class CreditCard(Card):
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def doSomething(self):
        return "Credit Card Class"
    
class DebitCard(Card):
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance
    
    def doSomething(self):
        return "Debit Card Class"

class BankCard(ATMcard, CreditCard, DebitCard):
    def __init__(self, pin, balance):
        ATMcard.__init__(self, pin, balance)
        CreditCard.__init__(self, pin, balance)
        DebitCard.__init__(self, pin, balance)

    def doSomething(self):
        return "Bank Card Class"
    

card = Card()
print(card.doSomething())  # Output: Card do something

atm_card = ATMcard(1234, 1000)
print(atm_card.doSomething())  # Output: ATM Class

credit_card = CreditCard(5678, 2000)
print(credit_card.doSomething())  # Output: Credit Card Class

debit_card = DebitCard(9012, 500)
print(debit_card.doSomething())  # Output: Debit Card Class

bank_card = BankCard(1111, 3000)
print(bank_card.doSomething())  # Output: Bank Card Class