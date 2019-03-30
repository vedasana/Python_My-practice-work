#1)Write a python function to find the max of three numbers.Without return
def  max() :
    a=int(input("Enter Number1 :"))
    b=int(input("Enter Number2 :"))
    c=int(input("Enter Number3 :"))
    if a>b and a>c :
        print(a,"is Max of three numbers")
    elif b>c:
        print(b,"is Max of three numbers")
    else:
        print(c,"is Max of three numbers")
max()
#1)_________________________________________
def  maxm() :
    a=int(input("Enter Number1 :"))
    b=int(input("Enter Number2 :"))
    c=int(input("Enter Number3 :"))
    Z=max(a,b,c)
    print(Z)
maxm()
#1)__________________
def max(a,b,c) :
    z=max(a,b,c)
    return z
m=max(10,20,30)
print(m)




#2)Write a python function to sum all numbers in a list.
#sample i/p:[8,2,3,0,7]
#Expected o/p: 20
def add():#WITHOUT USING RETURN & Defined List
    x=[5,9,3,6,2]
    z=sum(x)
    print(z)
add()
#___________________________________
def total (a):#WITH USING RETURN & Defined List
        sum=0
        for i in a:
                sum=sum+i
        return sum
x=[8,7,5,8,0,8]
k=total(x)
print("Total of ",x,"is :",k)

#________________________________________
def total(a):#WITHOUT USING RETURN  & Taking Values From End Users
        #global sum1
        sum1+=a
sum1=0
for i in range(1,6):
    n=int(input("Enter a number :"))
    total(n)
print("Total=",sum1)



#3)Write a python function to multiply all numbers in a list
#sample i/p:[8,2,3,-1,7]
#Expected o/p: -336
def mul() :#WITHOUT USING RETURN & Defined List
        mul=1
        x=[8,2,3,-1,7]
        for i in x:
                mul*=i
        print(mul)
mul()
#_____________________________________________________________________

def mul (k):#Multiply all numbers in a list_{WITH USING RETURN & Defined List
        mul=1
        for i in k:
                mul*=i
        return mul
y=[8,2,3,-1,7]
k=mul(y)
print("Total of ",y,"is :",k)
#_________________________________
def total (a):#Multiply all numbers in a list_{WITHOUT USING RETURN  & Taking Values From End Users
        global mul
        mul*=a
mul=1
for i in range(1,6):
    n=int(input("Enter a number :"))
    total(n)
print("Total=",mul)


#______________________________
def pro(a) :#Multiply all numbers in a list_{WITH USING Arguments & Taking Values From End Users}
        global mul
        mul*=a
        return(mul)
mul=1       
for i in range(1,6):
        n=int(input("Enter a number :"))
        k=pro(n)
print("Multiplication is",k)

   

#4)Write a python function to reverse string.Go to the editor
#sample i/p:"1234abcd"
#Expected o/p: "dcba4321"
def rev():#WITHOUT  USING Arguments  & Taking Values From End Users
    x=input("Enter a string :")
    y=x[::-1]
    print(y)
rev()
#_________________________________
def rev(a):#Reverse String_WITH USING Arguments & Taking Values From End Users
    y=a[::-1]
    return(y)
str=input("Enter a String :")
Reverse=rev(str)
print("Reverse of",str,"is :",Reverse)




#5)Write a python function to calculate the factorial of a number(a non negative integer).The function accepts the number as an argument
def fact():#WITHOUT  USING Arguments
        n=int(input("Enter a number :"))
        f=1
        for i in range(1,n+1):
                f=f*i
        print(f)
fact()
#________________________________________
def fact(g):#WITH USING Arguments & Taking Values From End Users
        f=1
        for i in range(1,n+1):
                f=f*i
        return f
        #print(f)
n=int(input("Enter a number :"))
#k=fact(n)
#print(k)
print(fact(n))  #instead of assigning a variable to calling function(eg :fact(n)),directly give print 



#6)Write a python function to check whether a number is in a given range.
def check()  :#WITHOUT  USING Arguments
        n=int(input("Enter a num :"))
        K=int(input("Enter a num to check :"))
        for i in range(1,n+1) :
                if K is i:
                        print(K,"is in the given range")
                        break
                        
        else:
                print(K,"is not in the given range")
check()
#___________________________________________________________
def checkrange(a,b):#WITH USING Arguments
        
        for i in range(1,n+1) :
                if m is i:
                        return True                        
        else:
            return False               
n=int(input("Enter a num for range :"))
m=int(input("Enter a num to check in range :"))
k=checkrange(m,n)
if k==True:
    print(m,"is in the given range")
else:
    print(m,"is not in the given range")




#7)Write a python function that accepts a string and calculate the number  of upper case letters and Lower case letters.
#Sample String 'The quick Brow Fox'
#sample i/p:3
#Expected o/p:12

def UL() :#WITHOUT  USING Arguments
    x=input("Enter a string : ")
    uc=0
    lc=0
    for i in x:
        if i.isupper()== True:
            #print("UpperCase Letters:",i)
            m=i.count(i)
            uc+=m
        elif i.islower()== True:
            #print("LowerCase Letters:",i)
             n=i.count(i)
             lc+=n              
    print(uc)
    print(lc)

UL()

#_______________________________________________________

def UL() :# Calculate the number of upper and Lower case letters_WITH USING Return
    x=input("Enter a string : ")
    global uc,lc
    for i in x:
        if i.isupper()== True:
            #print("UpperCase Letters:",i)
            m=i.count(i)
            uc+=m
        elif i.islower()== True:
            #print("LowerCase Letters:",i)
             n=i.count(i)
             lc+=n              
    #print(uc)
    #print(lc)
    return uc,lc

uc=0
lc=0
print("UpperCase Letters:",uc)
print("LowerCase Letters:",lc)




#8)Write a python function that  takes a list and returns new list with unique elements of the first list
#sample List :[1,2,2,3,3,3,3,4,5]
#Unique List: [1,2,3,4,5]

def ele():
    n=int(input("Enter a number for Elements in the List:"))
    k=[]
    for i in list(range(1,n+1)):
        n=int(input("Enter a value for list :"))
        k.append(n)
    print("sample List:",k)
    m=list(set(k))
    print("Unique List:",m)
ele()

#__________________________________________________________________

def ele():#WITH USING Return
    n=int(input("Enter a number for Elements in the List:"))
    k=[]
    for i in list(range(1,n+1)):
        n=int(input("Enter a value for list :"))
        k.append(n)
    print("sample List:",k)
    m=list(set(k))
    #print(m)
    return m
x=ele()
print("Unique List:",x)


#9)Write a python function that  takes a number as a parameter and check the number is prime or not

def prime():#WITHOUT USING Return
    n=int(input("Enter a number to check prime or not :"))
    if n>1:
        for i in range(2,n):
            if(n%i)== 0:
                print(n,"is not a prime number.")
                break
        else:
            print(n,"is a prime number.")
            
    else:
        print(n,"is neither prime number nor composite number.")
prime()

#________________________________________________________________________
def prime():#WITH USING Return
    if n>1:
        for i in range(2,n):
            if(n%i)== 0:
                break
        else:
            return 1
        return 0         
    else:
        return  10
        
n=int(input("Enter a number to check prime or not :"))
k=prime()
if k==1 :
    print(n,"is a prime number.")
elif k==0 :
    print(n,"is not a prime number.")
else :
    print(n,"is neither prime number nor composite number.")




#10)Write a python function to print the even numbers from a given list.
#sample List :[1,2,3,4,5,6,7,8,9]
#Expect: [2,4,6,8]


def eve():#WITHOUT USING Return
    n=int(input("Enter a number for giving range :"))
    s=[]
    e=[]
    for i in range(1,n+1) :
        m=int(input("Enter a number list element :"))
        s.append(m)
    print(s)
    for i in s:
        if (i%2)==0:
            e.append(i)
    print(e)
eve()

#_______________________________________________________
def eve():#WITH USING Return
    n=int(input("Enter a number for giving range :"))
    global s
    global e
    for i in range(1,n+1) :
        m=int(input("Enter a number list element :"))
        s.append(m)
    for i in s:
        if (i%2)==0:
            e.append(i)
    return s,e
s=[]
e=[]        
eve()
print("primary list : ",s)
print("Even Numbers list : ",e)




#11)Write a python function to check given string is palindrom or not

def pal():#WITHOUT USING Return
    x=input("Enter a string : ")
    if x==x[::-1]:
        print(x,"is palindrom")
    else:
        print(x,"is not a  palindrom")
pal()


#12)Write a python function to checkwhwather a string is a panagram or not

#For eg:"The quick brown fox jumps over the lazy dog"
import re#WITH USING Return
x=input("Enter a string : ")
x=x.lower()
alphas=re.findall("[a-z]",x)
print(alphas)
d={}
for i in alphas :
    cnt=alphas.count(i)
    d[i]=cnt
print(d)
print(len(d))
if len(d)==26:
    print("It is a panagram string.")
else:
    print("It is  not a panagram string.")
    

#13)Write a python that accepts a hypen-seperated sequence of words as input and prints the words  hypen
#seperated sequence after sorting them alphabetically.

#sample i/p:green-red-yellow-black-white
#Expected o/p:black-green-red-white-yellow

def hypen():#WITHOUT USING Return
    string=input("Enter hypen-seperated sequence of words :")
    print("-".join(sorted(string.split("-"))))
hypen()
#_________________________________________________________________

def hypen():#WITH USING Return 
    op="-".join(sorted(string.split("-")))
    #print(op)
    return op
string=input("Enter hypen-seperated sequence of words :")
c=hypen()
print("Expected output is :",c)







#******************************************************************************************************
#**********************************************{Recursive Programs}************************************



#Write a python program to find the sum of elements in a list recursively..!
  def SumOfElements():
    global total
    global i
    if i<len(x):
        total=total+x[i]
        i=i+1
        SumOfElements()
i=total=0
x=[2,5,6,8,1,6,2]
SumOfElements()
print(total)


#Write a python program to find the Fibonacci recursively..!
def fibonaci(next,prev):
   
    if next<=n:
        print(next)
        temp=next
        next=next+prev
        prev=temp
        fibonaci(next,prev)
        
n=int(input("Enter a number :"))
a=0
c=1
print(a)
print(c)
fibonaci(a+c,c)


#Write a python program to determine whether a given is even or odd.
def evenodd():
    
    if n%2==0:
        print(n,"is even")
    else:
        print(n,"is ODD")
    evenodd()
    
    
n=int(input("Enter a number :"))
evenodd()

    

#Write a python program to determine whether a given is even by using recursively..!
def evenodd():
    n=int(input("Enter a number :"))
    if n%2==0:
        print(n,"is even")
    else:
        evenodd()
evenodd()


#Write a python program to print even numbers in  a given List by using recursively..!

def even(i):
    if i<len(x):
        if x[i]%2==0:
            print(x[i])
        even(i+1)
x=[12,35,45,68,43,56,78,21,47,15,22]
k=0
even(k)
print(k,end="")



#Write a python program to determine how many times a given letter occuring in a string recursively



