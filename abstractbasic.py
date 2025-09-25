from abc import ABC,abstractmethod


class paymentmethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class CreditCard(paymentmethod):
    def pay(self, amount):
        print(f"Paid {amount} by using Credit Card")

class gpay(paymentmethod):
    def pay(self, amount):
        print(f"Paid {amount} by using Gpay")
class phonepay(paymentmethod):
    def pay(self, amount):
        print(f"Paid {amount} by using phonepay")
        
class debitCard(paymentmethod):
    def pay(self, amount):
        print(f"Paid {amount} by using Debit Card")

cc = CreditCard()
g = gpay()

cc.pay(100)  
g.pay(200)
