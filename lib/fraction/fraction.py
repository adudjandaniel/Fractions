class Fraction():
    '''A basic fraction data type in python'''

    def __init__(self, a=0, b=1):
        self.a = a
        self.b = b if b else 1

    def __str__(self):
        '''Converts the instance to a string'''
        return "{}/{}".format(self.a, self.b)

    def __repr__(self):
        '''View of the instance in console'''
        return self.__str__()

    def __add__(self, next_fraction):
        '''Adds two instances (+)'''
        new_numerator = self.a * next_fraction.b + self.b * next_fraction.a
        new_denominator = self.b * next_fraction.b
        return Fraction(new_numerator, new_denominator).simplified()

    def __sub__(self, next_fraction):
        '''Subtracts the second instance passed to the function from the first (-)'''
        new_numerator = self.a * next_fraction.b - self.b * next_fraction.a
        new_denominator = self.b * next_fraction.b
        return Fraction(new_numerator, new_denominator).simplified()

    def __eq__(self, next_fraction):
        '''Test equality (==)'''
        return self.simplified().__str__() == next_fraction.simplified().__str__()
    
    def __mul__(self, next_fraction):
        '''Multiply two instances (*)'''
        new_numerator = self.a * next_fraction.a
        new_denominator = self.b * next_fraction.b
        return Fraction(new_numerator, new_denominator).simplified()
    
    def __truediv__(self, next_fraction):
        '''Divide the first instance by the second (/)'''
        next_fraction = Fraction(next_fraction.b, next_fraction.a)
        return self.__mul__(next_fraction)
        
    def simplify(self):
        '''Simplify the fraction. Return None.'''
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
        '''Simplify the fraction. Return the simplified fraction.'''
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


