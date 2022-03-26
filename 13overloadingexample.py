#overloading==>for same operator we have different functions/opertions,will have different behaviour
#this is both example of overloading as well as polymorphism
#print(2+3)           #act as addition
#print('hi'+'hello')  #act as different i.e. concatenation

#Method Overloading

'''

class A:
    def calculate(self,x=None,y=None):
        if x!=None and y!=None:
            return x+y
        elif x!=None :
            return x**2
        else:
            return 0'''
'''
b=A()
b.calculate()
print('zero argument',b.calculate())
print('one argument',b.calculate(5))    #method overloading same function call with different number of parameters
print('two argument',b.calculate(3,2))
'''

#Operator Overloading
'''
class A:
    def __init__(self,num):             
        self.num=num

    def __add__(self,other):               #this method gets invoked when + operator used
        return self.num + other.num       #you can use any operator here instead of +

    def __eq__(self,other):
        if self.num==other.num:            #this method gets invoked when == operator use the call take it here
            return " equal"
        else:
            return 'not equal'
obj1=A(2)
obj2=A(3)
print(obj1.num)
print(obj2.num)
#print([1,2]+[3,4])  #list concatenation 
print(obj1+obj2)
print(obj1==obj2)
'''

#what is decorator in python blog

import random
print(random.randint(100,1000))