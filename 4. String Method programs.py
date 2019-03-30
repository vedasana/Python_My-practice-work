#1)Python program to Replace all occurrences of 'a'with '$ in a string'
#eg=Sailaja O/P:S$il$j$ 
x=input("Enter a string : ")
print(x.replace('a','$'))

or

x=input("enter a string : ")
x=x.replace('a','$')
print(x)


#2)Python program to remove the nth index char from a non-empty string
#eg:Sailaja, nth index eg:3 O/P:Saiaja
x=input("Enter a string : ")
if x!="":
    n=int(input("Enter nth index to remove : "))
    l=len(x)
    if n<l:
        x=x[ :n]+x[n+1: ]
        print(x)
    else:
        print("Oops Index is out of range")
else:
    print("Please enter a string")



    
#3)Python program to Form a new string  where the first Character and last character have been exchanged
#eg:Sailaja O/P:aailajaS
x=input("Enter a string : ")
if x!="":
    x=x[-1]+x[1:-1]+x[0]
    print(x)
else:
    print("Please enter a string")




#4) Python program to take in a string and replace every blank space with hyphen
    #eg: Welcome to python
    #Expected O/P:Welcome-to-python
x=input("Enter a Sentance : ")
if x!="":
    x=x.replace(" ","-")
    print(x)
else:
    print("Please enter a string")

--------------------------------------
x=input("Enter a Sentance : ")
x=x.split(' ')
print(x)
print(("_".join(x)))



    
#5)Python program to Remove characters of odd index values in a string
    #eg: Sailaja O/P:alj
x=input("Enter a string : ")
x=x[1::2]#x[ : :2]
print(x)



#6)Python program to Detect if Two strings are Anagrams
#Eg: anagram,nagaram,Both are anagram strings
#Eg: hello,world ,Both are nagaram strings
x=input("Enter a string1 : ")
y=input("Enter a string2 : ")
x= sorted(x)
y= sorted(y)
if x==y:
    print("Both are anagram strings")
else:
    print("Both are nagram strings")


    
#7)Python program to  Calculate Number of words and the Number of Characters present in a string
#Eg:Hello Good Morning to all
x=input("Enter a string : ")
Chars=(len(x))
words=len(x.split(" "))
print("Number of characters : ",Chars)
print("Number of words : ",words)



#8) Python program to count number of  Lowercase characters in a string
x=input("Enter a string : ")
c=0
for i in x:
    if i.islower():
        c=c+1
print("Number of lower case characters in a stringis :",c)


#9) Python program to check if a string ia palindrome or not
x=input("Enter a string : ")
if x==x[::-1]:
    print("Given String is polindrome")
else:
    print("Given String is polindrome")



#10)Python program to calculate the number of uppercase letters and  lower case letters  in a string
x=input("Enter a string : ")
lcnt=0
ucnt=0
for i in x:
    if i.islower():
        lcnt+=1
    elif i.isupper():
        ucnt+=1
print("Number of lower case characters in a stringis :",lcnt)
print("Number of upper case characters in a stringis :",ucnt)


#11)Python program to  Accept a Hyphen seperated sequence of words as input and print  the words in a Hyphen-seperated sequence after sorting them Alphabetically
#eg:hello-good-morning-to-all
#o/p:all-good-hello-morning-to
x=input("Enter a Hyphan seperated sequence of words  : ")
y=x.split('-')
print(y)
z=sorted(y)
print(z)
k="-".join(z)
print(k)

#12)Python program to count the number of characters(characters frequency) in a string
#Eg:google.com
#O/P: {o:3,g:2,'.':1,e:1,l:1,m:1,c:1}

x=input("Enter a string")
print("Length of x is:",len(x))
y={}
print(type(y))
for i in x: 
    if i in y: 
        y[i]+= 1
    else: 
        y[i] = 1
print ("Count of all characters in is:",y)

#________________________________________________________(or)

x=input("Enter a string")
print(len(x))
y=sorted(x)
print(y)
d={}
for i in set(y):# for set it wont displays duplicate value & its unordered list
#for i in y:# for dictionary it displays duplicate value
    print(i,".",x.count(i))
    d[i]=x.count(i)
print(d)
#----------------------------------(or)
x=input("Enter a string")
d={}
for i in set(x):
    d[i]=x.count(i)
print(d)
#---------------------------------(or)
x=input("Enter a string")
y=sorted(x)
for i in set(y):# for set it wont displays duplicate value & its unordered list
#for i in y:# for dictionary it displays duplicate value
    print(i,".",y.count(i))


#13)Python program to count the Occurrences of each word in a given string sentence
#eg: Python is simple and it is easy
#O/P:{'python':1,'is':2,'simple':1,'and':1,'easy':1}

x=input("Enter a string")
x=x.split(' ')
y=sorted(x)
for i in set(y):# for set it wont displays duplicate value & its unordered list
#for i in y:# for dictionary it displays duplicate value
    print(i,".",y.count(i))
    
#------------------------------------------------------(or)
x=input("Enter a string")
print("Length of x is:",len(x))
x=x.split(' ')
y={}
print(type(y))
for i in x: 
    if i in y: 
        y[i]+= 1
    else: 
        y[i] = 1
print ("Count of all characters in '" ,x, "' is:",y)
print(y)


#14)Python program to check if substring is present in a given string
#Eg: python is simple and it is easy,simple.
#O/P: simple present in a given string.
x=input("Enter a string")
y=input("Enter sub string")
if y in x:
    print("substring is present in a given string")
else:
    print("substring is not present in a given string")

#15. Write a python program to get a string made of first 2 & last 2 chars from a given string
#    if the string length is lessthan 2, returns instead of the empty string

#sample string: "Saranya"
#Expected String: "Saya"

#sample string:"Sa"
#Expected String: "SaSa"

#sample string: S
#Expected String: Empty String

x=input("Enter a string")
if len(x)>=2:
    print(x[ :2]+x[-2: ])
else:
    print("String is empty")
    
#16. Write a python program to get a string from a given string where all occurrences of its 1st char have been changed to $
# except the 1st char it self
#sample: "restart"
#expected o/p: "resta$t"
x=input("Enter a string")
print(x[0]+x[1: ].replace(x[0],'$'))


#17. Write a python program to get a single string from given two strings,
#seperated by space& Swap 1st two chars of each string
#sample: 'abc','xyz'
#expected o/p: xyc abz
x=input("Enter 1st string")
y=input("Enter 2nd string")
print((y[ :2]+x[2: ]),' ',x[ :2]+y[2: ])

#18. Write a python program to add "ing" at the end of a given string(Length should be at least 3)
#If the given string already ends with 'ing', Then add "ly" instead .
# If the length of the given string is lessthan 3 leave it as it is unchanged.
#sample: 'abc'
#expected o/p: 'abcing'

#sample: 'string'
#expected o/p: 'stringly'

#sample: 'W3'
#expected o/p: 'W3'
x=input("Enter a string")
if len(x)>=3:
    if x[-3: ]!='ing':
        print(x+"ing")
    elif x[-3: ]=='ing':
        print(x+'ly')
else:
    print(x)



#19)Write a Python program that takes a list of words seperated by comma and returns the length of the longest one.
#Sample String : 'hello,good,morning,to,everyone
#Expected Result 'everyone' 
#Sample String : "warm,wishes,to,python,and,devops,class"
#Expected Result : 'wishes'
    
x=input("Enter a list of words  : ")
y=x.split(",")
print(y)
z=[len(i) for i in y]
print(z)
big=max(z)
print(big)
if z.count(big)==1:
    print(y[z.index(big)])
else:
    y=[y[i] for i,j in enumerate(z) if j==big]
    print(max(y))
#1.-----------------------------------------------------------
x=input("Enter a list of words  : ")
x=x.split(',')
print(x)
a=''
print(len(a))
for i in x:
    if len(i)>len(a):
        a=i
print(a)

#2.-----------------------------------------------------------
x=input("Enter words").split(',')
y=x[0]
for i in x:
    if len(i)>len(y):
        y=y.replace(y,i)
        #y=i
print(y)
#3.------------------------------------------------------------------------------------------------------------------------------------------ 
#20) Write a Python script that takes input from the user and displays that input back in upper and lower cases.
x=input("Enter a string")
print(x,"in uppercase",x.upper())
print(x,"in lowercase",x.lower())


#21. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
#Sample words: red, white, black, red, green, black 
#Expected Result : black,green, red, white,red 

x=input("Enter a sequence of words").split(',')
print(sorted(set(x)))


#22). Write a Python program to create the HTML string with tags around the word(s).
#Sample String : 'V, 'Python'
#Expected Result : <i>Python</i>'
x=input("Enter a string")
print("<i>"+x+"</i>")
#1------------------------------
a=input("Enter a tag:")
b=input("Enter a string to enter a tag:")
html_tags="<"+a+">"+b+"</"+a+">"
print(html_tags)
#2-------------------------------

#23.Write a Python program to insert a string in the middle of a string.
#Sample String : 'Python'
#Expected Result [[Python]],{{Python}}
x=input("Enter a string:")
#print("[[",x,"]]",",","{{",x,"}}")
str1="[["+x+"]]"
str2="[["+x+"]]"
print(str1)
print(str2)


#24)Write a python program to get a string made of 4 copies of the last two characters of a specified string(length must be atleast 2).
#Sailaja
#jajajaja
x=input("Enter a string")
if len(x)>=2:
    print(x[-2: ]*4)
else:
    print("Enter minimum 2 digit number")

#------------------------------------------------------------------------------------------------------------------------------------------ 

#25) Write a Python program to reverses a string if its length is multiple of 4.
x= input("Enter a string :")
if len(x)%4==0:
    print(x[: : -1])
else:
    print(x,"is not multiple of 4")

#------------------------------------------------------------------------------------------------------------------------------------------ 

#26)Write a Python program to convert a given string to a11 uppercase if it contains at least 2 uppercase characters  in the first 4 Characters.
x= input("Enter a string :") #HyDerabad
if len(x)>=4 :
    cnt=0
    for  i  in  x[:4] :
        if i.isupper() :cnt+=1
    if cnt>=2:
        print(x.upper())
    else :
        print(x)
else :
    print("Enter minimum 4 characterlength string")

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Not yet completed****
x=input("Enter a string")
if len(x)>=4:
    y=x.split()
    y=x[ :4]
    z=list(y)
    for i in z:
        cnt=0
        if i not in "ABCDEFGHIJKLMONPQRSTUVWXYZ":
            print("No uppercase characters in given string")
        else:
            cnt+=1
            if cnt==2:
                z=''.join(z)
                print(z.upper())
            else:
                print("string should contain min 2 uppercase characters")
          
else:
    print("Length of the string should be greaterthan 4")

#------------------------------------------------------------------------------------------------------------------------------------------ 
#27) Write a Python program to check whether a string starts the following characters(d,v,k,$)
x= input("Enter a string to check whether a string starts the following characters(d,v,k,$) :")
if x[0].lower() in 'dvk$':
    print("Yes the string first letter is : ",x[0])
else:
    print("The string first characters not starting with [d,v,k,s]letters")

#------------------------------------------------------------------------------------------------------------------------------------------  
#28) Write a Python program to reverse words a string.
x= input("Enter a sentance :")
y=x.split()
for  i in y:
    print(i[: : -1],end=" ")
#Or------------------------------------
x= input("Enter a sentance :").split()
y=[i[::-1] for i in x]
x=" ".join(y)
print(x)
#Or------------------------------------
x= input("Enter a sentance :")
x=x.split()
print(x)
for i in x:
    print(i[::-1],end=' ')
#Or------------------------------------
x= input("Enter a sentance :").split()
for i in x:
    y=i[::-1]
    print(''.join(y),end=' ')


#------------------------------------------------------------------------------------------------------------------------------------------  
#29) Write a Python program to check a string contains alphabets or alphanumeric. 
x= input("Enter a string :")
if  x.isalpha():
    print(x,'has only alphabets')
else:
    print(x,"has  alphanumeric chars")

#------------------------------------------------------------------------------------------------------------------------------------------
#30)Write a python program to convert a string in a list.
x= input("Enter a string :")
print(list(x))

#--------------------------------------------------------------------------------------
#31)Write a Python program to remove spaces from a given string.
x= input("Enter a string :")
print(x.replace(" ",""))

#--------------------------------------------------------------------------------------
#****
#32) Write a python program to find the maximum occurring character in a given string.

x= input("Enter a string :")
x=sorted(x)
print(x)
y={}
for i in x:
    if i in y:
        y[i]+=1
    else:
        y[i]=1
print(y)
z={a:b for b,a in y.items()}# To exchange dictionay keys and values
print(z)
maxi=max(z.keys())
print("the maximum occurring character in a given string is:",z[maxi]#my work
#Or-----------------------------------------------------------------------------
x= input("Enter a string :")
chars=list(x)
d1={}
for  i in chars :
     cnt=chars.count(i)
     d1[i]=cnt
print(d1)
max1=max(d1.values())
for  i,j in d1.items() :
    if j==max1:
        print(i)
#---------------------------------------------------------------------------------------------
#33) Write a python program to capitalize first last letters of each word of a given string.
x= input("Enter a string :").split()#hello good  morning to all
y=[i[0].upper()+i[1:-1]+i[-1].upper() for i in x]
print(y)
#or--------------------------------------------------------------------
x=input("Enter a string").split(' ')
print(x)
for i in x:
    y=i[0].upper()+i[1:-1]+i[-1].upper()
    print(y,end=' ')
#or--------------------------------------------------------------------
x= input("Enter a string :").split()#hello good  morning to all
for i in x:
    y=[i[0].upper()+i[1:-1]+i[-1].upper()]#[]--> to print list of words
    print(y,end=' ')

#------------------------------------------------------------------------------------------------------------------------------------------
34) Write a Python program to remove duplicate characters of a given string.
x= input("Enter a string :")
x=''.join(set(x))
print(x)
#------------------------------------------------------------------------------------------------------------------------------------------'''

#python program to form a new string where the first character and last
#character have been exchanged
#given string:python
#expected output:nythop

x=input("enter a string : ")
if x!="":
    x=x[-1]+x[1:-1]+x[0]
    print(x)
else:
    print("plz enter a string : ")
#or----------------------------------
x=input("enter a string : ")
print(x[-1]+x[1:-1]+x[0])

#Remove double occured elements from the given string
x="a p q u r s a i h q p" 
y=[]
z=[]
for i in x:
    print(i)
    if i in y:
        z.append(i)
    else:
        y.append(i)
print('y is :',y)
print('z is :',z)
y=set(y)
z=set(z)
k=(y-z)
print(k)
for i in k:
    print(i,end=' ')

#____________________________or
x="a h g d u k l k k h h a a j s"
y=[]
z=[]
for i in x:
    if i not in y:
        y.append(i)
    elif i in y:
        z.append(i)

print(set(y)-set(z))
    
    
