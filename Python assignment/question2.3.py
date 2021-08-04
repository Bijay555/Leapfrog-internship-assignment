# Custom Error implemented using class

class HandlingError(Exception):
    def __init__(self, num):
        self.value = num
  
    def __str__(self):
        return(repr(self.num))
  
try:
    raise(HandlingError(3*2))  
# Value of Exception is stored in error
except HandlingError as error:
    print('An exception has occured:  ',error.value)



# Custom Error using Exception or BaseException class using message to handle at least two of the cases.
class MarkError(Exception):
    def __init__(self, mark,  message='Marks should be between 30 to 90'):
        self.mark = mark
        self.message = message
        super().__init__(self.message)

x=99
if not (30 < x < 90):
    raise MarkError(x)

class MsgNotFound(Exception):
    pass
try:
    raise MsgNotFound("Because of error")
    pass

except MsgNotFound as err:
    print("Message Not found",err)

ab = MsgNotFound()
print(ab)


# Full fledged case for exception handling using try, except, else, finally
def div(n, m):
    try:
        a = n // m
        print("Answer is :", a)
    except ZeroDivisionError as err:
        print("Sorry ! You are dividing by zero ", err)
    except TypeError as er:
        print("Sorry! this is type error",er)
    else:
        print("No error occured")
    finally:
        print("This statement is always printed ")
   
div(6, 2)
div(3, 0)
div(14,3)
div('aa',3)