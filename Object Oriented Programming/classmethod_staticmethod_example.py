class FixedFloat:
    def __init__(self, amount):
        self.amount = amount
    
    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)

new_number = FixedFloat.from_sum(19.575, 0.789)        
print(new_number)

class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'
    
    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'

money = Euro.from_sum(18.786, 9.999)        
print(money)