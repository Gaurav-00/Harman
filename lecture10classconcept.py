#oops concept  in python
'''everything is object in python i.e list,tuple,dictionary,function
 for build a car toy mould==>number of car toys
 '''
'''
class Student:
   
    pass  #future use

print(Student)

print(dir(Student))
print(Student.__doc__)
'''
class Student:
    '''This is student class 
    you are learning concepts'''
    Studentcount=0              #class variable  whenever instance created increase the count
    def __init__(self,name,dept):
        self.name=name         #when you want to perform an operation when instance is created write it in a constructor
        self.dept=dept
        Student.Studentcount+=1   #you not using self as it is declare outside a constructor
    
    '''def calc(self,x,y): #self argument is mandatory when you are writing method
        return x+y                   #   inside a class else your method not work'''
    def printname(self):
        print('name of student is',self.name,self.dept )    
    def printCount(self):
        print('no of students:',Student.Studentcount)  # to count no of student created
stud1=Student('Rajesh','IT')

stud2=Student('gss','comp')
stud1.printname()
stud2.printname()
#print(stud1.calc(1,2))
stud1.name='Vicky'   #overwriting attributes
stud1.printname()

stud1.printCount()
del stud2.name
print(stud2.name)
