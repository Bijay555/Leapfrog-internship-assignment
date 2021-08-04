# Create an iterator for square numbers 
class Square_num:
    def __init__(self, num):
        self.num = num
        self.sq = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.sq >= self.num:
            raise StopIteration
        
        self.sq+=1
        return self.sq**2

a = Square_num(5)
for i in a:
    print(i)


# Generator for square numbers
def squares_num(num):
    for n in range(1, num+1):
        yield n ** 2
        
number = 5
square = squares_num(number)
for s in square:
    print(s)
    
    