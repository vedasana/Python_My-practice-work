#LIST ASSIGNMENTS:

#x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]
#1)WAP FInd length of  given list without using len() function.
x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]
cnt=0
for i in x:
    cnt+=1
print("Length =",cnt)



    
#2)WAP to find  SUM of elements without using Sum()Function
x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]
sum=0
for i in x:
    sum=sum+i
print("Sum of elements in a list :",sum)



#3)WAP to find  MAX element without using max()Function
x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]
max=x[0]
for i in x:
    if i>max :
        max=i
print(max)
#--------------or
x=sorted(x)
print(x[-1])


#4)WAP to find  Min element without using min()Function
x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]
min=x[0]
for i in x:
    if i<min :
        min=i
print(min)
#--------------or
x=sorted(x)
print(x[0])


#5)WAP Accept a number and display its index without using index() method.
x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]
n=int(input("Enter a number to search index : "))
if n in x :
    for i,j in enumerate(x):
        if j==n :
            print(n,"found at",i,"index in a list")
else:
        print(n,"element notfount  in the list ")




        
#6) WAP accept a element and count total no of occurences  without using count() method.
x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,903,3,3]
n=int(input("Enter a number to  : "))
cnt=0
for i in x:
    if i == n:
        cnt+=1
print(cnt)




#7) WAP print above list elements in reverse order without using reverse() method.
x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,903,3]
print(x[: : -1])
#-----------------------------------------Or
x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,903,3,3]
for i in reversed(x):
    i=0# just to give print out of the loop and not get indentation error
print(list(reversed(x)))
#----------------------------------------or
x.reverse()
print(x)

    
#8)WAP store all 1 digit number into one list and 2  digit numbers into another list and 3 digit numbers into another list
#other remaining numbers into another list display
x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]
a=[]
b=[]
c=[]
d=[]
for i in x:
    if i<=9:
        a.append(i)
    elif i>=10 and i<=99:
        b.append(i)
    elif i>=100 and i<=999:
        c.append(i)
    else:
        d.append(i)
print(a)
print(b)
print(c)
print(d)
#----------------------------------------------------------------------Or

x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90,10,45432]
a=[]
b=[]
c=[]
d=[]
for i in x:
    if i<=10:
        a.append(i)
    elif 10<=i<100:
        b.append(i)
    elif 100<=i<1000:
        c.append(i)
    else:
        d.append(i)
print(a)
print(b)
print(c)
print(d)


   
#9)WAP store even numbers into one list and odd numbers into another list
x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]
e=[]
o=[]
for i in x:
    if i % 2==0:
        e.append(i)
    else:
        o.append(i)
print(e)
print(o)



#10)WAP accept a element and remove the given element from a list without using remove() method.
x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]
n=int(input("Enter a  element to remove : "))
if  n in x:
    temp=[]
    for i in x:
        if i!=n:
            temp.append(i)
    x=temp
    print(x)
else:
    print(n,"Element not in the list ")
#x=['UNIX','LINUX','AWS','PERL','PYTHON','JAVA','PERL','LINUX','DEVOPS']
#_----------------------------------------------------------------or
x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]
n=int(input("Enter a  element to remove : "))
print(len(x))
z=[]
y=[]
for i in x:
    if i==n:
        y.append(i)
    else:
        z.append(i)
print(z)
print(len(z))


#--------------------------------------or
x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]
x.remove(200)
print(x)



#11) WAP print whatever elements ending  with 's' character
x=['UNIX','LINUX','AWS','PERL','PYTHON','JAVA','PERL','LINUX','DEVOPS']
for i in x:
    if i[-1]=="S":
        print(i,',',end='')



        
#12) WAP whatever elements begining with vowel characters.
x=['UNIX','LINUX','AWS','PERL','PYTHON','JAVA','PERL','LINUX','DEVOPS']

for  i in x:
    if i[0] in "AEIOU":
        print(i)




#13)WAP whatever elements length more than 5 characters
x=['UNIX','LINUX','AWS','PERL','PYTHON','JAVA','PERL','LINUX','DEVOPS']
for i in x:
    if len(i)>5:
        print(i)


#14)WAP delete  all duplicate elements
x=['UNIX','LINUX','AWS','PERL','PYTHON','JAVA','PERL','LINUX','DEVOPS']
y=[]
for i in x:
    if i not in y:
        y.append(i)
print(y)


#15)WAP display only duplicate elements
x=['UNIX','LINUX','AWS','PERL','PYTHON','JAVA','PERL','LINUX','DEVOPS']
y=[]
for i in x:
    if x.count(i)>1 and i not in y:
        y.append(i)
print(y)


#16)WAP display only non duplicate elements
x=['UNIX','LINUX','AWS','PERL','PYTHON','JAVA','PERL','LINUX','DEVOPS']
y=[]
z=[]
for i in x:
    print(i)
    if i in y:
        z.append(i)
    else:
        y.append(i)
print(y)
print(z)
y=set(y)
z=set(z)
k=(y-z)
print(k)


#17)WAP take x list and y list common elements and write into z list
x=['UNIX','LINUX','AWS','PERL','PYTHON','JAVA','PERL','LINUX','DEVOPS']
y=['C','C++','UNIX','PYTHON','DBA','.NET','AWS']
z=[]
for i in x:
    if i in y:
        z.append(i)
print(z)


#18)WAP take x list and y list non-common elements and write into z list

x=['UNIX','LINUX','AWS','PERL','PYTHON','JAVA','PERL','LINUX','DEVOPS']
y=['C','C++','UNIX','PYTHON','DBA','.NET','AWS']
z=[]
x=set(x)
y=set(y)
z=x.union(y)
w=x&y
print(z)
print(w)
print(z-w)



#####################################################################################################



#1) Python program to find the second largest number in a list
x=[5,2,5,23,622,622,33,35,6,3,6]
x=sorted(list(set(x)))
print("The second Largest number in the list is : ",x[-2])
#________________Or

x=[5,2,5,23,622,622,33,35,6,3,6]
y=sorted(set(x))
print(y)
print(y[-2])


#2) Python program to Merge two lists and sort it.
x=[5,2,5,23,622,33,35,6,3,6]
y=[1,2,3,4,5,6,8,9]
z=x+y
print(sorted(z))


#3) Python program to sort a list according to the length of the elements
x=['sailaja','saranya','swetha','Trishya','Sathvika','veda','sarani','sai']
y=[len(i) for i in x]
print(y)
y.sort()
print(x)
print(y)
for i in y:
    for j in x[:]:#*
        if i==len(j):
            print(j,',',end='')
            x.remove(j)
#To substitute elements we use[:],To not to repeat the same value because of index change...
#[:]-Every time it will take original x only, Not updated x, Here x is constant,If we dont put[:]
#It will take updated x, for every iteration, which will lead bugs



#4) Python program to find union of two lists.
x=[1,2,3,4,5,6,7,8,9]
y=[10,11,12,13,14,15,16,17,18,19]
w=set(x)
#print(w)
z=set(y)
#print(z)
#k=z.union(w)
k=z|w
print(k)



#5) Python program to Find the Intersection of two lists.
x=[1,2,3,4,5,6,7,8,9,19]
y=[10,11,12,13,14,15,16,17,18,19]
w=set(x)
#print(w)
z=set(y)
#print(z)
#k=z.intersection(w)
k=z&w
print(k)



#6) Python program to create a list of tuples with the first element as the number and the second element as the square of the number.
x=[(i,i**2) for i in list(range(1,11))]
print(x)
#x=[(i,i*i) for i in range(1,10)]
#print(x)
#______________________________________
x=[3,45,3,2,1,34,5,3,8]
y=[]
for i in x:
    j=i,i*i
    print(j)
    y.append(j)
print(y)


#7)Python program to Find all numbers in a range which are  perfect squares and sum of all digits in the number is less than 10.
x=[]
for i in range(1,101):
    sqroot=i**0.5
    sq=int(sqroot)*int(sqroot)
    if i==sq:
        x.append(i)
print(x)
for i in x:
    c=0
    for j in str(i):
        c+=int(j)
    if c<10:
        print(i,end=",")




#8)Python program to Generate Random numbers from from 1 to 20 and append them to the  list
x=[]
import random
for i in range(1,21):
    y=random.randint(1,20)
    x.append(y)
print(x)



#9)Python program to sort a list of Tuples in Increasing order by the last element in each Tuple

x=[(2, 4),(1, 1),(4, 16), (3, 9),(5, 25)]
y={}
for i in x:
    y[i[-1]]=i[0]
print('y is:',y)
s=sorted(y)
sorted(s)
print('Sorted:',s)
a=[]
for i in s:
    print(y[i])
    a.append((y[i],i))
print(a)

#____________________________________or

x=[(2, 4),(1, 1),(4, 16), (3, 9),(5, 25)]
a=[]
y=dict(x)
print(y)
z={a:b for b,a in y.items()}
print(z)
s=sorted(z.keys())
print(s)
for i in sorted(z):
    k=(z[i],i)
    a.append(k)
print(a)




#10)Python program to swap the first and last value of the list.
x=[5,2,5,23,622,33,35,6,3,6]
x[0],x[-1]=x[-1],x[0]
print(x)



#11)write a python program to count the number of strings where the string length is 2 or more and the first  and last characters are same from the given list of strings
#Sample list:['abc','xyz','aba','1221']
#expected result: 2
x=['abc','xyz','aba','1221']
count=0
for i in x:
    if len(i)>=2 and i[-1]==i[0]:
        print(i)
        count=count+1
print(count)



#12)write a python program that takes 2 lists and return true if it has atleast one common number.
import random
x=[]
y=[]
for i in range(1,10):
    x.append(random.randint(1,10))
    y.append(random.randint(1,10))
print(x)
print(y)
for i in x:
    for i in y :
        print("Yes, there are common elements.")
        break
else:
    print("There are no Common Elements")
#___________________________________________(Or)
x=['sailaja','veda','vani']
y=['Nikhita','veda','vani']
z=set(x)&set(y)
print(z)
if len(z)>=1:
    print(True)
else:
    print(False)

    
#13)write a python program to print a specified list after removing the 0th,4th,and 5th elements
#Sample list:['Red','Green','white','Black','Pink','Yellow']
#expected result: ['Green','white','Black']
x=['Red','Green','white','Black','Pink','Yellow','Purple']
a=x[0]
b=x[4]
c=x[5]
x.remove(a)
x.remove(b)
x.remove(c)
print(x)

#Just like this[:],  Assign the element to remove to a variable so that it will remove the required value exactly.
#To substitute elements we use[:],To not to repeat the same value because of index change...
#[:]-Every time it will take original x only, Not updated x, Here x is constant,If we dont put[:]
#It will take updated x, for every iteration, which will lead bugs


#14)write a python program to print the number of a specified list afer removing even numbers from it.
x=[5,4,5,6,9,6,644,511,8445]
y=[]
for i in x[:]:
    if i%2==0:
        #x.remove(i)
        y.append()
        print()
print(y)
print(len(x))


#15)write a python program to shuffle and print a specified list.
from random import shuffle
x= ['Red', 'Green', 'White', 'Black', '4654',4646,45636,766,8765,'Pink', 'Yellow']
print(len(x))
shuffle(x)
print(x)
print(len(x))


#16)write a python program to generate and print a list of first and last 5 elements,
#where the values are square of numbers between 1 and 30(both included).
y=[]
z=[]
import random
for i in range(1,31):
    x=random.randint(1,31)
    y.append(x) 
print('y:',y)
#print(len(y))
for i in y:
    z.append(i*i)
print('z:',z)
#print((len(z)))
print("List of first and last 5 elements:"z[:5]+z[-5:])
#______________________________________________________
# for  1 to 30 numbers:      
x=[]
for i in range(1,31):
    x.append(i*i)
print(x)
print(x[0:5]+x[-5:])



#17))write a python program to generate and print a list except for  the first 5 elements,
#where the values are square of numbers between 1 and 30(both included).
import random
x=[]
for i in range(1,31):
    x.append(random.randint(1,1000))
print('x=',x)
y=x[5:]
print('y=',y)
z=[i*i  for i in range(1,31)]
print('z=',z)
for i in y:
    if i in z:
        print('i=',i,end=' ')
#-----------------------------------------
import random
y=[]
z=[]
for i in range(1,31):
    x=random.randint(1,31)
    y.append(x)
print(y)
print(len(y))
for i in y:
    z.append(i*i)
print(z[5:])



#18)write a python program to get the difference between the two lists.
import random
x=[]
y=[]
for i in range(1,10):
    x.append(random.randint(1,10))
    y.append(random.randint(1,10))
print('x=',set(x),type(x))
print('y=',set(y))
z=set(x)-set(y)
print('z type is:',type(z))
print(list(z))



#19)write a python program to convert a list of characters into a string
x=['s','a','i']
for i in x:
    print(i,end="")



#20)write a python program to select an item randomly from a list.

import random
x=['sai','sailu','sailaja','vani','veda']
print(random.choice(x))



#21)write a python program to get the frequency of the elements in a list.
x=[5,6,9,642,5,9,2]
y={}
for i in x:
    y[i]=x.count(i)
print(y)



#22)write a python program to check wheather a list contains a sub list.
#x=[['sai','sailu','sailaja'],[3,5,7],['vani','veda'],[4,4]]
x=[2,6,9,6,6,[44,55],'sailaja','saranya']
for i in x:
     if  type(i) is list :
        print("list contains a sub list")
        break
else:
        print("list has no sub list")



#23)write a python program to create  a list by concatenating a given list which range goes from 1 to n.
    #sample list :['p','q']
    #n=5
    #output : ['p1','q1','p2','q2','p3','q3','p4','q4','p5','q5']
x=['p','q']
y=[]
for i in x:
    for j in range(1,6):
        print("'",str(i)+str(j),"'",',',end =' ')




#24)write a python program to convert a list of  multiple integers into a single integer
#Sample list:[11,33,50]
#Expected O/P:113350
x=[4,56,525,744444444,55]#How to take a list of elements from end users
for i in x:
    print(i,end='')
    


#25)write a python program to split a list based on first character of word.
x=['Agni','Jal','Vayu','Bhumi','AAkash']
x=sorted(x)
for i in x:
    print(i[0],end=' ')
    







