class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
    
    def add_money(self, deposit_dollar, deposit_cents):
        self.dollars += deposit_dollar
        if self.cents + deposit_cents <= 99:
            self.cents += deposit_cents
        else:
            self.dollars += int((self.cents+deposit_cents)/100)
            self.cents = (self.cents+deposit_cents - int((self.cents+deposit_cents)/100)*100)

    
pig = PiggyBank(1, 1)
print(pig.dollars, pig.cents)

pig.add_money(500, 500)

print(pig.dollars, pig.cents)