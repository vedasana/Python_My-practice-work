#1

def main():
    print("Hai")
main()




#2
def main():
    print("Hai")
if __name__== "__main__":
    main()
print("Hello")




#3
a=10
a='wfEF'
print(a)
print("BABA"+"123")




#4
x="Hello"
print(x)
def someFunction():
    x="1275"
    print(x)
someFunction()
print(x)




#5

x="Hello"
print(x)
def someFunction():
    global x
    print(x)
    x="1275"
    print(x)
someFunction()
print(x)
print(x) #It changes global variable



#6
a=10
print(a)
del (a)


#7
var1 = "Guru99!"
var2 = "Software Testing"
print ("var1[0]:",var1[0])
print ("var2[1:5]:",var2[1:5])



#8
x = "Hello World!"
print(x[:6]) 
print(x[0:6] + "Guru99")



#9
oldstring = 'I like Guru99' 
newstring = oldstring.replace("like", "love")
print(newstring)


#10
string="PYTHON at guru99"
print(string.lower())


#11
string="PYTHON at guru99"
print(string.upper())



#12
string="python at guru99"		
print(string.capitalize())


#13
print("_".join("Veda"))


#14
print("_".join (reversed("Veda")))


#15
string="12345"		
print(" ".join(reversed(string)))


#16
a="12345"		
print(a[ : :-1])


#17
a=12345		
print(str(a)[ : :-1])


#18
x="Veda Saranya 123"
print(x.split('a'))


#19
x="Hello"
print(x)
x=x.replace("H","A")
print(x)


#20
def main():
     print("hello world!")
main()
print("Guru99")

x=2
y=4 
print(x*y)

#21
print(''.join(reversed("1234567")))


#22
txt = "     Hello World   jkh"
print(txt)
x = txt.rstrip()
print(x)


#23
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]

fruits.update(more_fruits)
print(fruits)

#24
x="hello\nhello\n\
hai"
print(x)
y='This is also a \nperfect example\
of\nmulti-line comments'
print(y)

z=(2+3+4+
   4+1+2)
print(z)

#25
print(isinstance("veda",int)) # To check boolean


#26
d1={'sailaja':'good','saranya':'Smart'}
print (d1['saranya'])


#27
x=("Hello","Hai",125,"Bye",456,"Best",'Bolo',3,2)
print(x)
print(type(x))
print(x[3])
x=(234);
print(x)


#28
a = {'x':100, 'y':200}; b = list(a.items())
print(a)
print(b)
print(type(b))


#29
x=1,2,"sana",345,"\hello"
print(x)
print(type(x))
y="\"hello"
z="\hello"
print(y)
print(z)


#30
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}	
studentX=Boys.copy()
studentY=Girls.copy()
print(studentX)
print(studentY)


#31
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print((Dict['Tiffany']))



#32
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
Dict.update({"Sarah":9})
print(Dict)


#33
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
del Dict ['Charlie']
print(Dict)


#34
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("Students Name: %s" %list(Dict.items()))
print("Students Name:" %list((Dict.items())))
print("____")
print(list(Dict.items()))
print(type(list(Dict.items())))
print(Dict.items())
print(type(Dict.items()))
print("____")
print("Students Name:",list(Dict.items()))
print("Students Name:",list(Dict))
print("Students Name:",Dict.items())

#35
print("_".join(("Veda","345","Sailu")))

print("_".join(("Veda","Sana")))


#36
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
Y=list(Dict.items())
print(Y)
X= list(Dict.keys())
X= list(Dict)#We can give directly to get only keys, No need to mention ".keys"
print(X)
X.sort()
print(X)
''''for k in X:
    if k in list(Boys.keys()):
        print((":".join((k,str(Dict[k])))),"_",True)
    else:print(k,"_",False)'''
    
for k in X:
    if k not in list(Boys):
        print(k,"_",str(Dict[k]),":",True)
    else:print(k,":",False)



#37
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
Students = list(Dict)#(or)list(Dict.keys())
Students.sort()
print(Students)
for S in Students:
      print(":".join((S,str(Dict[S]))))




#38
Marks={"veda":87,"Nandu":82,"Veena":90,"Yugansh":89,"Deepika":87,"Sarika":63,"Avinash":92}
sisters={"veda":87,"Veena":90,"Deepika":87,"Sarika":97}
brothers={"Nandu":82,"Yugansh":89,"Avinash":92}
x=list(Marks)
print(x)
x.sort()
print(x)
for i in x:
    if i in brothers:
        print(i,"_",Marks[i],"_","Brothers list")
    else:
        print("_".join((i,str(sisters[i]))),"_","sisters list")



#39
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print(len(Dict))
print(type(Dict))
print(str(Dict))
x=Dict
print(x)
x=list(Dict)
x.sort()
print(x)
for i in x:
    print(i,Dict[i])


#40
x=4
y=5
print(x>y)
num1=4
num2=5
print(("Line 1 - Value of num1 : ", num1))
print(("Line 2 - Value of num2 : ", num2))


#41 
x = 4
y = 8
list = [1, 2, 3, 4, 5 ];
if ( x in list ):
   print("Line 1 - x is available in the given list")
else:
   print("Line 1 - x is not available in the given list")
if ( y not in list ):
   print("Line 2 - y is not available in the given list")
else:
   print("Line 2 - y is available in the given list")


#42
v = 4
w = 5
x = 8
y = 2
z = 0
z=(v+w)*x/y;   
print("Value of (v+w) * x/ y is ",  z)




#43 Python_Funtion:
def Func():
    print("Hello")
    print("Hi")
Func()
print("Baba")
print(Func())



#43(1)

def multiply(x=2,y=9):  #On the function side it is a parameter
    return x*y  #On the calling side, it is an argument
print(multiply())

#2
def multiply(x=2,y=9):
    return x*y
print(multiply(3))#It will take updated x value as 3

#3
def multiply(x,y=9):
    return x*y
print(multiply(4))#It will take x value as 4

#4
def multiply(x,y=0):
    return x*y
print(multiply(3,7))

#5
def multiply(x,y):
    return x*y
print(multiply(4,5))

#6
def multiply(x=3,y=9):
    return x*y
print(multiply(y=2,x=3))#Reversed the order of x,y


#7
def multiply(x,y):
    return x*y
print(multiply(y=5,x=6))#Reversed the order of x,y

#8
def multiply(x,y):#We don't have any specific function to run over 
    return x*y
print(multiply)#Here, It returns a default location value 0x02E4B8E8 



#43(2)
def Hello(*args):#By using wild card character
    print(args)
Hello(1,2,3,4,5,6)#We can pass multiple arguments




#44
total=70
x=("AUS","USA","AUPST")
country="AUPST"
if country in x:
    if country=="AUS":
        if total <= 50:
            print("Shipping Cost is  $50")
        elif total <= 100:
            print("Shipping Cost is $25")
        elif total <= 150:
            print("Shipping Costs $5")
        else:
            print("FREE Shipping")
    if country == "USA": 
        if total <= 50:
            print("Shipping Cost is  $100")
        else:
            print("FREE")
else:
    print("No shipping")





#45
def main():
    x=0
    while(x<7):
        print(x)
        x = x+1
main()

#1
def main():
    x=0
    while(x<7):
        if x==2:
            x = x+1
            continue
        print(x)
        x=x+1
        
main()

#2
def main():
    x=0
    while(x<7):
        if x==5:
            x = x+1
            break
        print(x)
        x=x+1
        
main()


#46
for x in range(2,7):
    print(x)


#47
months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"]
for i in months:
    print(i)



#48
for i in range(5,20):
    if (i==10): continue
    #if (i==15): continue
    print(i)


#49
for x in range (10,20):
    #if (x == 15): break
    if (x % 5== 0) : continue
    print(x)


#50
months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"]
for e, i in enumerate (months):
    print(e+1,")",i)



#51
for i in '123':
 print (i)
 
 

#52
#Python_Class
 
class myClass():
    def method1 (self):
        print ("Guru99")
    def method2 (self,someString): 
       print ("Software Testing:" + someString)

def main():
    h=myClass()
    h.method1()
    h.method2("sdgf")
main()



#53
class myclass():
    def method1(One):
        print("1 is first number")
    def method2(One):
        print("2 is second number")
    def method3(One):
        print("3 is third number")
    def method4(Four):
        print("4 is fourth number")
    def method5(Five,SomeInfo):
        print("5 is fifth number",SomeInfo)
def main():
    x=myclass()
    x.method1()
    x.method2()
    x.method3()
    x.method4()
    x.method5("555")
print("jbdjbsajb")
main()




#54
class myclass():
    def method1(Hi):
        print("My SaiBaba is great")
    def method12(Hi):
        print("So that,")
    def method2(Hi):
        print("Save me")
    def method3(Hi,string):
        print("I am Happy"+ string)
def main():
    x=myclass()
    x.method1()
    x.method2()
    x.method3("Please")
main()




#54(1)
class veda():
    def sub1(self):
        print("Hello, World!!")
    def sub2(self):
        print("Welcome to Robotic automation")
    def sub3(self,Hello):
        print("Lot of opportinuties here, "+Hello)

def main():
    veda().sub1()
    veda().sub2()
    veda().sub3("Enjoy, Robotics")
main()
        


#Inheritance:

#55
#Example:1

class Dad():
    def method1(One):
        print("I am Daddy")
class Baby(Dad):
    def Submethod1(One):
        #1.D=Dad()
        #D.method1()
        #2.Dad().method1()
        #3.Dad.method1(One);
        #4.Dad.method1(One)
        print ("child Class Method1")
    def Submethod2(One):
        print("child Class method2")     
def main():
    #5.D=Dad()
    #D.method1()
    #6.Dad.method1(Dad)
    Dad().method1()
    B=Baby()
    B.Submethod1()
    B.Submethod2()
main()



#56
#Example:2

class myClass():
  def method1(self):
      print("Guru99")
class childClass(myClass):
    def method1(self):
        myClass.method1(self);
        print ("childClass Method1")
    def method2(self):
        print("childClass method2")     
def main():           
  # exercise the class methods
  c2 = childClass()
  c2.method1()
  c2.method2()
main()



#Constructor

#57
class myclass():
    def __init__(self,One,Two,Three,SomeInfo):
        self.One=One
        self.Two=Two
        self.Three=Three
        self.SomeInfo=SomeInfo
t=myclass(1,"Sana",27,"Years")
print(t.One,t.Two,t.Three,t.SomeInfo)

#58
class veda:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
v=veda(1,"Sana",27,"Years")
print(v.a,v.b,v.c,v.d)

#59
class User:
    name=""
    def __init__(self,name):
        self.name=name
    def sayHello(self):
        print("Welcome to Guru99, "+self.name)
U=User("Veda")
U.sayHello()


#60
class User():
    def __init__(self, name, Age):
        self.name=name
        self.Age=Age
    def sayHello(self):
        print("Welcome to my blog, " +self.name + self.Age)
U=User("Veda","_27 years old")
U.sayHello()

#61

class veda:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def sayHello(self):
        print("Welcome to Guru99",self.a,self.b)#58+59
v=veda(1,"Sana",27,"Years")
print(v.a,v.b,v.c,v.d+"Hello")
v.sayHello()

#62

class veda:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
v=veda(1,"Sana",27,"Years")
print(v.a,v.b,v.c,v.d+"Hello",v.a)

class veda:
    def sayHello(self):
        print("Welcome to Guru99",self)
v=veda()
v.sayHello()

