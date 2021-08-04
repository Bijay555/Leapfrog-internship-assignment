
'''Create at least 4 classes having semantic meaning (having relation to each other) so that multiple inheritance can be achieved and incorporating following things in some of them:
@classmethod 
@staticmethod
@property and setter for it
Dunder methods __str__ and more…
Class_variable
'''
class A:
    class_variable = 'hello'
    def __init__(self,name,value):
        self.name = name
        self.value = value
        
    def __str__(self):
        return "This is parent class"
    
    def printValue(self):
        print(self.value)

    @staticmethod
    def isValue(value):
        return value>25
    
    @classmethod
    def useString(cls,string):
        name,value = string.split(',')
        value = int(value)
        return A(name,value)
    
    @property
    def anything(self):
        return 'the name is '+ self.name + 'and the value is '+ str(self.value)

    @anything.setter
    def anything(self, aws):
        self.name, self.value = aws.split(',')
        self.value = int(self.value)


class B(A):
    def __init__(self, bname, bvalue=45):
        print(bname, "has a value 45")
        super().__init__(bname, bvalue)

class C(A):
    def __init__(self, cname, cvalue):
        print(cname, "has a value", cvalue)
        super().__init__(cname, cvalue)

class D(B,C):
    def __init__(self):
        print("Jack has value 43")
        super().__init__('jack', 43)

ab = D()
b = A('Bijay', 60)
print(b.isValue(b.value))
print(str(b))
