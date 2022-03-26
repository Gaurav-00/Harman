#Inheritance==>acquire the properties of your parent(base)class


#Parent class
'''class Animal:
    def speak(self):
        print("animal is speaking")


#child class
class Lion(Animal):        #child class able to access all variable and methods of parent class
    def roar(self):
        print("lion is roaring")'''
'''
simba=Lion()
simba.roar()   #output-:lion is roaring
print(dir(simba))
simba.speak()   #output-:Animal is speaking
'''

#Multilevel Inheritance==   animal==>lion=>cub  

'''class cub(Lion):
    def walk(self):
        print('cub is walking')'''
'''
cu=cub()
print(dir(cub))
cu.roar()
cu.walk()
cu.walk()
'''
#MUltiple Inheritance
'''
class calc1:
    def addition(self,a,b):
        print( a+b)
class calc2:
    def multiplication(self,a,b):
        print(a*b)

class calc3(calc1,calc2):
    def sub(self,a,b):
        print( a-b)
'''
'''
a=calc3()
print(dir(a))
a.sub(5,4)
a.multiplication(5,4)
a.addition(5,4)
print(issubclass(calc3,calc1))
print(issubclass(calc3,calc2))
print(isinstance(a,calc3))
print(isinstance(a,calc1))
'''
'''
class A:
    def sp(self):
        print('i am from class A')

class B:
    def sp(self):
        print('i am from  class b')

class C(A,B):              #it first check method in  c then a and then in b 
    def st(self):
        print('i am from c')

c=C()
print(dir(c))
c.sp()
print(C.mro())   #tell about order of execution
#method Resolution order  ==>First check in C and then check in A and then in B i.e. from left to right


#Method Overriding

class D(A):
    def sp(self):
        print(' I am from D')
g=D()
g.sp()'''

#method overloading and opertaor overloading

#Data Abstraction ==>Hiding data from user
'''
class Student:
    count=0

    def __init__(self):
        Student.count +=1
    def printcount(self):
        print('count is:',Student.count)

stud1=Student()
stud2=Student()
stud2.printcount()'''

#we want to abstract count ,want to hide variable count ,we use __variable_name
class Student:
    __count=0

    def __init__(self):
        Student.__count +=1
    def printcount(self):
        print('count is:',Student.__count)

stud1=Student()
stud2=Student()
stud2.printcount()
#print(stud1.__count)   #thus we are hiding __count from a user use can see here

#to get abstract value we use this method
print(stud1._Student__count)    #to acess them outside the class
#print(stud1.__count)

#to get example for super() function
#to abstractusing===> _variable_nm,__variable_nm
