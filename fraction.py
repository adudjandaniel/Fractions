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
        return self.simplified().__str__() == next_fraction.simplified().__str__()
            
    def simplify(self):
        a = self.a
        b= self.b
        while True:
            if a == b:
                gcd = a
                break
            elif (a == 0 and b) or (a and b == 0):
                gcd = b if b else a
                break
            elif a > b:
                a %= b
            else:
                b %= a
        
        self.a = int(self.a / gcd)
        self.b = int(self.b / gcd)
    
    def simplified(self):
        a = self.a
        b= self.b
        while True:
            if a == b:
                gcd = a
                break
            elif (a == 0 and b) or (a and b == 0):
                gcd = b if b else a
                break
            elif a > b:
                a %= b
            else:
                b %= a
        
        a = int(self.a / gcd)
        b = int(self.b / gcd)
        
        return Fraction(a,b)

#af1 = Fraction(1,3)
#f2 = Fraction(2,5)
#f3 = Fraction(9,27)


#f4 = f1 + f2
#f5 = f1 - f2



#print(f1,'+',f2, '=', f4)
#print(f1,'-',f2, '=', f5)
#print(f1 == f3)
#print(f3)
#print(f3.simplified())
#print(f3)

