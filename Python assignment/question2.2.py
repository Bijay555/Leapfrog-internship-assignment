# Decorators with parameters
 
def xyz(func):
  print("we are inside xyz()")
 
  def abc(*args, **kwargs):
    print("we are inside abc function")
    print("Decorated the abc")
    
    func() 
  return abc

def mno():
    print("we are inside mno()")
xyz(mno)()


# Decorator  without parameter
def deco(func):
    print('this is deco function')
    def inside_deco(*args, **kwargs):
        print('this is inside_deco function')
        print('this is most protected area')

        func()
    return inside_deco

@deco
def outside_deco():
    print('This is outside_deco function')

outside_deco()




















# def decorator_fun(func):
#   print("Inside decorator")
 
#   def inner(*args, **kwargs):
#     print("Inside inner function")
#     print("Decorated the function")
#     # do operations with func
     
#     func()
     
#   return inner
 
# @decorator_fun
# def func_to():
#     print("Inside actual function")
 
# func_to()
