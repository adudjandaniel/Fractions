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
        return Fraction(new_numerator, new_denominator).simplified()

    def __sub__(self, next_fraction):
        new_numerator = self.a * next_fraction.b - self.b * next_fraction.a
        new_denominator = self.b * next_fraction.b
        return Fraction(new_numerator, new_denominator).simplified()

    def __eq__(self, next_fraction):
        return self.simplified().__str__() == next_fraction.simplified().__str__()
            
    def simplify(self):
        a = self.a
        b= self.b
        if b > a:
            a, b = b, a
        while b != 0:
            remainder = a % b
            a, b = b, remainder
        gcd = a
        
        self.a = int(self.a / gcd)
        self.b = int(self.b / gcd)
    
    def simplified(self):
        a = self.a
        b= self.b
        if b > a:
            a, b = b, a
        while b != 0:
            remainder = a % b
            a, b = b, remainder
        gcd = a
        
        a = int(self.a / gcd)
        b = int(self.b / gcd)
        
        return Fraction(a,b)

#f1 = Fraction(1,8)
#f2 = Fraction(3,4)
#f3 = Fraction(970,10)

#print(f3.simplified())
#print()
#f4 = f1 + f2
#print(f4)
#f5 = f2 - f3
#print(f5)



#print(f1,'+',f2, '=', f4)
#print(f1,'-',f2, '=', f5)
#print(f1 == f3)
#print(f3)
#print(f3.simplified())
#print(f3)

