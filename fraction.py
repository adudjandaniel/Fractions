class Fraction():
    
    def __init__(self, a=0, b=1):
        self.a = a
        self.b = b if b else 1
        
    def __str__(self):
        return "{}/{}".format(self.a, self.b)
    
    def __repr__(self):
        return self.__str__()
    
    def __add__(self, next_fraction):
        new_numerator = self.a * next_fraction.b + self.b * next_fraction.a
        new_denominator = self.b * next_fraction.b
        return Fraction(new_numerator, new_denominator)
    
    def __sub__(self, next_fraction):
        new_numerator = self.a * next_fraction.b - self.b * next_fraction.a
        new_denominator = self.b * next_fraction.b
        return Fraction(new_numerator, new_denominator)
    
    def __eq__(self, next_fraction):
        multiplier = next_fraction.a / self.a
        new_numerator = round(self.a * multiplier, 6)
        new_denominator = round(self.b * multiplier, 6)
        return new_numerator == next_fraction.a and\
            new_denominator == next_fraction.b
    
f1 = Fraction(1,3)
f2 = Fraction(2,5)
f3 = Fraction(9,27)

f4 = f1 + f2
f5 = f1 - f2



print(f1,'+',f2, '=', f4)
print(f1,'-',f2, '=', f5)
print(f1 == f3)