#1)Write a python program to read data from a given file.
x=open("sai.txt","w")
x.write("Sailaja  is learning python.\n")
x.write("Sailaja  is learning JAVA .\n")
x=open("sai.txt","r")# We can read only if the file is exists.Otherwise it goes to IOE Error.
a=x.read()
print(a)    
x.close()


#2)Write a python program to find size of a given file.
with open("sai.txt",'r') as x:
    a=x.read()
print("Size of a given file : " ,len(a))
                                                            #OR
import os 
print(os.path.getsize("sai.txt"))


#3)Write a python program to count total number of lines  in a given file.
with open("sai.txt","r") as x:
    z=x.readlines()
    print("Total number of lines  in a given file",len(z))



#4)Write a python program to display nth line from a given file.
n=int(input("Enter a number for nth line : "))
with open ("sai.txt",'r') as x:
    a=x.readlines()
    l=len(a)
    print(l)
    if l>n:
        print(a[n-1])
    else:
        print("out of range")



#5)Write a python program to count no of empty lines in a given file.
with open ("sai.txt",'r') as x:
    a=x.readlines()
    print(a)
    print(a.count('.\n')) 



#6)Write a python program to display 1st five and last five lines from a given file
with open ("sai.txt","r") as x:
    a=x.readlines()
    a=a[:5]+a[-5:]
    print(a) 
    


#7)Write a python program to display 1st 10 characters and last 10 characters from a given file.
with open ("sai.txt","r") as x:
    a=x.read()
    print(a)
    print(" First 10 characters : ",a[:11] + " ,\n " + "Last 10 characters :",a[-10:])
     


#8)Write a python program to count how many times the given word occured in a given file.
n=input("Enter a word in the file : ")
with open("sai.txt",'r') as x:
    a=x.read()
    if n in a :
        print(a.count(n))
    else:   
        print("Please, Enter the word existing in the file")
#_______________________________________________________________
n=input("Enter a word :")
c=0
with open ("Dummy.txt",'r') as x:
    a=x.read()
    a=a.split(' ')
    print(a)
for i in a:
    if n in i:
        c+=1
        print(c)
     


#9)Write a python program to display unique lines from a given file.
with open("sai.txt","r") as x:
    k=x.readlines()
    print(set(k))



#10)Write a python program to delete a given word from a given file.
n=input("Enter a word to delete from the file : ")
with open("sai.txt","r") as x:
    y=x.read()
    k=y.replace(n,"")
    with open("sai.txt","w") as z :
        z.write(k)
        #z=print(y.replace(n,""))       


#11)Write a python program write each and every line first and last words into another file with comma seperator.
with open("sai.txt","r") as x:
    y=x.readlines()
    print("y= ",y)
z=open ("Sailu.txt","w")
for i in y:
        k=i.split(' ')
        print("k= ",k)
        p=k[0]+","+k[-1]
        z.write(p)
        print("p= ",p)
z.close()



#12)Write a python program display all given word lines from a given file.
n=input("Enter a word : ")
with open("sai.txt","r") as  x:
    y=x.readlines()
    for i in y:
        if n  in i:
            print(i)
    else:
       print("The word you entered is not in the file ")


#13)Write a python program to display which are the lines having exactly 5 words
with open("sai.txt","r") as  x:
    y=x.readlines()
    for  i in y:
       k=i.split(" ")
       if  len(k)==5:
           print(i)
#____________________________________
with open("Dummy.txt",'r') as x:
    y=x.readlines()
    for i in y:
        z=i.split(' ')
        if len(z)==5:
            print(z)


#14)Write a python program to display alternative lines from a given file.
with open("sai.txt","r") as  x:
    y=x.readlines()
    for  i in y:
        print(i)
    print(y[::2])
#______________________
with open("Dummy.txt",'r') as x:
    y=x.readlines()
    z=y[::2]
    print(z)
    for i in z:
        print(i)



#15)Write a python program sort given file contents.
with open ("sai.txt","r") as x:
    y=x.readlines()
    y.sort()
    print(y)
with open ("sai.txt","w") as x:
    x.writelines(y)
#---------------------------------
with open("Dummy.txt",'r') as x:
    y=x.readlines()
    z=sorted(y)
    print(z)
for i in z:
    print(i,end='\n')



#16)Write a python program swap each line first and last words and write  into another file.
with open  ("sai.txt","r") as x:
    y=x.readlines()
    for i in y:
        #print("i = ",i)
        p=i.split(" ")
        #print(p)
        #print(p[-1],p[1:-1],p[0])
        p[0],p[-1]=p[-1].rstrip("\n"),p[0]
        print(p)

#______________________________________________
with open ("Dummy.txt",'r') as x:
    y=x.readlines()
    print(y)    
with open ("sai.txt",'w') as z:
    for i in y:
        k=i.split(' ')
        k[0],k[-1]=k[-1].rstrip("\n"),k[0]
        print(k)
        print(" ".join(k))



#17)Write a python program display which are the lines starting with "error" word in a given file.
with open("sai.txt","r") as x:
    y=x.readlines()
    for i in y:
        #print(i)
        m=i.split()
        if m[0]=="Error":
            print(i)



#18)WAP accept a file and check the given file exist or not.
import os
fn=input("Enter a file :")
if os.path.exists(fn):
        print("The file is Exists")
else:
    print("The file is not Exists")
    


#18.1) WAP to delete an existing file.
import os
os.remove("veda.txt")



#19)WAP accept a file and displays its file type.

import os
fn=input("Enter a file :")
if os.path.isfile(fn):
    print("It is a file")
elif os.path.isdir(fn):
    print("It is a directory")

#*********************************************************************************************************************
mkdir()#To make a directory
chdir()#To change directory
getcwd()#To get current working directory
listdir()#To get list of sub directories
rmdir()#To remove a directory/To delete a directory
# If we did not mention a path, It will take path of current directory randomly

import os
os.mkdir("Dad")#Creates directory in curreent directory location
os.mkdir("E:\Hello")#Creates directory at given location
os.chdir("E:\zzzz")# To change current directory to required directory
os.mkdir("E:\zzzz")#mkdir-To Create directory
os.chdir("E:\zzzz")#chdir-To Change directory
print(os.getcwd())#To get current directory path
print(os.listdir('E:\ABCD'))#To get the list of all sub directories in given directory
print(os.listdir())#To get the list of all sub directories in current directory
os.rmdir("E:\zzzz")#To delete directory in the given path
os.rmdir("Hello")#It will delete the directory with given name only if its exists in current directory location
#*********************************************************************************************************************
#20)WAP accept a directory and count total no.of files.

import os
f=input("Enter a file :")
g=[]
x=os.listdir(f)
os.chdir(f)
for i in x:
    if os.path.isfile(i):
        print(i)
        g.append(i)
print(len(g))
#________________________________________
import os
fn=input("Enter a directory :")
cntf=0
if os.path.exists(fn):
    if os.path.isdir(fn):
        a=os.listdir(fn)
        os.chdir(fn)
        for i in a:
            if os.path.isfile(i):
                print('File:',i)
                cntf+=1
print("cntf",cntf)


#21)WAP accept a directory and count total no.of files and directories
import os
fn=input("Enter a directory :")
cntf=0
cntd=0
if os.path.exists(fn):
    if os.path.isdir(fn):
        a=os.listdir(fn)
        os.chdir(fn)
        for i in a:
            if os.path.isdir(i):
                print("Dir:",i)
                cntd+=1
            if os.path.isfile(i):
                print('File:',i)
                cntf+=1
print("cntf",cntf)
print("cntd",cntd)  
#_____________________________________
import os
fn=input("Enter a directory :")
cntf=0
cntd=0
a=os.listdir(fn)
print(a)
print(os.getcwd())#C:\Users\Saranya\Desktop
os.chdir(fn)#Change directory is to change the directory to required directory
print(os.getcwd())#C:\Users\Saranya\Desktop\Wipro
for i in a:
    if os.path.isdir(i):
        print("Dir:",i)
        cntd+=1
    if os.path.isfile(i):
        print('File:',i)
        cntf+=1
print(os.getcwd())
print("cntf",cntf)
print("cntd",cntd)
#_____________________________________
import os
fn=input("Enter a directory :")
if os.path.exists(fn):
    if os.path.isdir(fn):
        print(len(os.listdir(fn)))
#__________________________________or
import os
fn=input("Enter a directory :")
print(len(os.listdir(fn)))


#import os.path
#import os
#print(os.path.join(os.sep,'home','user','work'))
#\home\user\work

#print(os.path.split('/usr/bin/python'))
#('/usr/bin', 'python')
#print(os.getcwd())
#print(os.path.curdir)

#**************************************************************************************************************************************************
#22.WAP Accept a directory and display only all .py files
import os
fn=input("Enter a directory : ")
if os.path.exists(fn):
    if os.path.isdir(fn):
        print(os.listdir(fn))
        for i in os.listdir(fn):
            if i.endswith(".py"):
                print(i)

#23)WAP Accept a directory  and display all empty file.
import os
fn=input("Enter a directory : ")
#print(os.getcwd())
if os.path.exists(fn):
    if os.path.isdir(fn):
        os.chdir(fn)
        #print(os.getcwd())
        files=os.listdir(".")
        for   i  in files :
            if os.path.isfile(i) :
                size=os.path.getsize(i)
                if size==0 :
                    print(i)
#____________________________________________
import os
fn=input("Enter a directory : ")
print('1',os.getcwd())#1 C:\Users\Saranya\Desktop
files=os.listdir(fn)
#print(files)
os.chdir(fn)
print('2',os.getcwd())#2 C:\Users\Saranya\Desktop\Wipro
files=os.listdir('.')# To list files& directories in present directory; If we give here (fn) it will take path as:
                     #C:\Users\Saranya\Desktop\Wipro\wipro. Which leads to FileNotFoundError. Then we should give the path directly at input,
                     #If we also have sub directory/folder with name (fn)
                     #then we wont get error and it will take the sub directory/folder and search for empty files in it
print('3',os.getcwd())#3 C:\Users\Saranya\Desktop\Wipro
#print(files)
for i in files:
    if os.path.isfile(i):
        y=os.path.getsize(i)
        if y==0:
            print(i)

#**************************************************************************************************************************************************

#24)WAP Accept a file  and count total no.of characters,total no.of words and total no.of lines.
import os
fn=input("Enter a File : ")
with open (fn,'r') as x:
    x=x.readlines()
cnt=0
for i in x:
    i=i.split(' ')
    #print(i)
    #print(len(i))
    cnt+=len(i)
print('Total no of characters:',os.path.getsize(fn))
print('Total no of words:',cnt)
print('Total no of lines:',len(x))
#_________________________________________________________
import os
fn=input("Enter a File : ")
if os.path.exists(fn):
    if os.path.isfile(fn):
        #os.chdir(fn)
        #files=os.listdir(".")
        #print(files)
        #print("True")
        with open(fn,"r") as x :
            data=x.readlines()
        print("Totalno.oflines :",len(data))
        print("total no.of chars :",os.path.getsize(fn))
        wcnt=0
        for i in data:
            i=i.split(" ")
            wcnt=wcnt+len(i)
        print("Total no.of words:",wcnt)


#25)WAP Accept a file  and string and delete the  string from a file.
import os
f=input("Enter a File : ")
s=input("Enter a String : ")
with open(f,"r") as x:
    y=x.read()
    print(y)
    if s in y:
        z=y.replace(s,'')
        print(z)
#______________________________Or
import os
fn=input("Enter a File : ")
str=input("Enter a String : ")
if os.path.exists(fn):
    if os.path.isfile(fn):
        with open(fn,"r") as x:
            y=x.read()
            if str in y:
                z=y.replace(str," ")
                print(z)
      


#26) Write a python script accept a file and string , if given string found then read data from given string to end of the file.

import os
fn=input("Enter a File :")
str=input("Enter a string :")
if os.path.exists(fn):
    if os.path.isfile(fn):
        with open (fn,'r') as x:
            y=x.read()
            if str in y:
                z=y.find(str)
                print(z)
                print(y[z:])
             
#_________________________________________
import os
f=input("Enter a File :")
s=input("Enter a string :")
with open (f,'r') as x:
        y=x.read()
        if s in y:
            z=y.find(s)
            print(y[z:])

#27) Write a python script and delete duplicate lines from a file.
import os
fn=input("Enter a File :")
if os.path.exists(fn):
    if os.path.isfile(fn):
        with open (fn,'r') as x:
            y=x.readlines()
            for i in set(y):
                print(i)

#_______________________________
import os
fn=input("Enter a File :")
if os.path.exists(fn):
    if os.path.isfile(fn):
        with open (fn,'r') as x:
            y=x.readlines()
            z=set(y)
            for i in z:
                if i!="\n":
                    print(i)
#________________________________
import os
f=input("Enter a file")
with open (f,'r') as x:
    x=x.readlines()
    for i in set(x):
        if i!="\n":
            print(i)



#28) Write a python script delete empty lines from a give file.
with open ("sai.txt",'r') as x:
    a=x.readlines()
    print(a)
    print(a.count('.\n')) # to count empty lines
#________________________________________________
import os
fn=input("Enter a File : ")
if os.path.exists(fn):
    if os.path.isfile(fn):
        with open (fn,"r") as x:
            y=x.readlines()
            print('y=',y)
            print(len(y))
            for i in y:
                if i!="\n":
                    print("i=",i)
#___________________________________
import os
f=input("Enter a file")
with open (f,'r') as x:
    x=x.readlines()
    for i in x:
        if i!="\n":
            print(i)

               


#29)Write  a python script accept a file and display each line last word.

import os
fn=input("Enter a file : ")
if os.path.exists(fn):
    if os.path.isfile(fn):
        with open (fn,"r") as x:
            y=x.readlines()
            for i in y:
                k=i.split(" ")
                print(k[-1])
#_____________________________________
import os
f=input("Enter a file:")
with open (f,"r") as x:
    x=x.readlines()
    for i in x:
        y=i.split(' ')
        print(y[-1])
 


#30) write a python script accept a file and display file contents in sorted order.

import os
fn=input("Enter a File : ")
if os.path.exists(fn) and os.path.isfile(fn):
    with open (fn,"r")as x:
        y=x.readlines()
        for i in sorted(y):
            print(i)
#___________________________________________________
import os
f=input("Enter a file:")
with open (f,"r") as x:
    x=x.readlines()
    y=sorted(x)
    for i in y:        
        print(i)


#31) Write a python script accept file and reverse the file contents.

filename=input("Enter file name: ")
for line in reversed(list(open(filename))):
    print(line.rstrip())
#______________________________________________
import os
fn=input("Enter a file : ")
with open (fn,"r") as x:
    x=x.readlines()
    y=reversed(x)
    for i in y:
        print(i)
#_____________________________________________
import os
fn=input("Enter a file : ")
with open (fn,"r") as x:
    x=x.readlines()
    y=reversed(x)
    for i in y:
        if i!='\n':#Removes empty lines
            print(i.rstrip())# rstrip removes line space
#___________________________________________________________
#______________________________________________________________
import os,sys
fn=input("Enter a file : ")
with open (fn,"r") as x:
    x=x.readlines()
    for i in x:
        y=i.split(' ')
        #print(y)
        z=(y[: :-1])
        k=' '.join(z)#Add space at the end of the each line in file, Then it works
        print(k.rstrip('\n'))#No need of rstrip 


#32) Write python script accept a directory and add the following messge at end of each file in a given directory.
#("Thank you for Joining with us.")
import os
dn=input("Enter a directory name : ")
x=os.listdir(dn)
os.chdir(dn)
for  i in x:
    if os.path.isfile(i):
        with open (i,"a") as y:
            y.write("\nSai Baba")

#____________________________________________
import os
dn=input("Enter a directory name : ")
print(os.getcwd())
x=os.listdir(dn)
os.chdir(dn)
print(os.getcwd())
print(x)
for  i in x:
    if os.path.isfile(i):
        with open (i,"a") as y:
            y.write("\nSai Baba")
#__________________________________________________
import os,sys#sys is to pass argument
dn=input("Enter a directory name : ")
#msg=input("Enter Greetings to send:")
if os.path.exists(dn) and os.path.isdir(dn):
    #os.chdir(dn)
    print(os.getcwd())
    x=os.listdir(dn)#   os.listdir(".") If it is in current directory.
    os.chdir(dn)
    print(os.getcwd())
    print(x)
    for  i in x:
        if os.path.isfile(i):
            with open (i,"a") as o1:
                o1.write("\n******************\n")
                #o1.write("HAPPY RADHA SAPTAMI")
                #o1.write(msg)
                o1.write(sys.argv[1])
                o1.write("\n******************\n")
    else:
            print("No such Dir")



                

#33) write a python script accept a file and diplay frequency of words in dictionary format.
import os
fn=input("Enter a  File  : ")
if os.path.exists(fn) and os.path.isfile(fn):
    with open(fn,"r") as x:
        y=x.read()
        k=y.replace("\n"," ")
        z=k.split(" ")
        d1={}
        for i in set(z):#Here no need of set
            d1[i]=z.count(i)
        print(d1)
#__________________________________________________
import os
fn=input("Enter a  File  : ")
if os.path.exists(fn) and os.path.isfile(fn):
    with open(fn,"r") as x:
        y=x.read()
        k=y.replace("\n"," ")# Next line wont continue here
        x=k.split(' ')
        #print(x)
        d={}
        for i in x:
            d[i]=x.count(i)
print(d)



#34) Write a python script accept a file and string and count total no of occurences.
import os
fn=input("Enter a File : ")
str=input("Enter a String :")
if os.path.exists(fn) and os.path.isfile(fn):
    with open (fn,"r") as x:
        y=x.read()
        z=y.count(str)
        print(z)
#___________________________________________________
import os
f=input("Enter a File : ")
s=input("Enter a String :")
with open (f,"r") as x:
    x=x.read()
    print(x)
    y=x.count(s)
    print(y)



#35) Write a python script create given no of directories in the current directory.
import os
n=int(input("Enter no.of directories to create : "))
#dn=input("Enter directory name : ")
for i in range (1,n+1):
    dn=input("Enter directory name : ")
    os.mkdir(dn)
#_____________________________________________________
import os
n=int(input("Enter no.of directories to create : "))
for i in range (1,n+1):
    d=input("Enter directory name : ")
    print(os.getcwd())
    os.chdir("E:/ABCD")#To create given no of directories in the required directory
    os.mkdir(d)
    print(os.getcwd()) 



#36) Write a python script to copy a file.
import os
sfn=input("Enter a File : ")
dfn=input("Enter a File : ")
if os.path.exists(sfn) and os.path.isfile(sfn):
    with open (sfn,"r") as x:
        y=x.read()
    with open (dfn,"w") as x:
        x.write(y)
    print("File Copied")
else:
    print("File not Copied")
#___________________________________________________
s=input("Enter a source file :")
d=input("Enter a destination file :")
with open (s,'r')as x:
    x=x.read()
with open (d,'w') as y:
    y.write(x)
    print(y)



#36a) Write a python script to rename a file.
    
import os
a='Dummy.txt'
b='a.txt'
os.rename(a,b)



#37) Write a python script to move a file.

import os
s=input("Enter a source file :")
d=input("Enter a destination file :")
with open (s,'r')as x:
    x=x.read()
with open (d,'w') as y:
    y.write(x)
    print(y)
os.remove(s)
#____________________________________________________
import shutil
s='Dummy.txt'
d='Sai.txt'
shutil.move(s,d)
#______________________________________________________
import shutil, os
files = ['Dad.txt', 'Sai.txt', 'Mom.txt']
for f in files:#To move more files to a certain folder
    shutil.move(f, 'Wipro')



#38) Write a python script accept 2 files and concatenate  files data and store into 3rd file.
import os
f1=input("Enter a File1 : ")
f2=input("Enter a File2 : ")
f3=input("Enter a File3 : ")
if os.path.exists(f1) and os.path.isfile(f1):
    if os.path.exists(f2) and os.path.isfile(f2):
        with open (f1,"r") as x:
            y=x.read()
        with open (f3,"w") as x:
            x.write(y)
        with open (f2,"r") as x:
            y=x.read()
        with open (f3,"a") as x:
            x.write(y)
    else:
        print("No such files")


#39) Write a python script accept a directory nil-count total no.of  files and total no.of directories.







#40) Write a python script accept a directory and list which file are sizes more than 1000 bytes.


                                                                                                                                              
#41)  WAP accept 2 files and display common records in both files 





#42) WAP accept    2 files and diplay opposite records from both files




#43) WAP accept 2 files and join horizOnatily with "-" delimeter.

fn1=input("Enter a  filename1 :")
fn2=input("Enter a  filename2 :")
import os
if os.path.exists(fn1) and os.path.isfile(fn1):
    if os.path.exists(fn2) and os.path.isfile(fn2):
        with open (fn1,"r") as x:
            f1=x.readlines()
        with open(fn2,"r") as x:
            f2=x.readlines()
        l1=len(f1)
        l2=len(f2)
        temp=[]

        if l1>l2:
            for i in range(l2):
                k=f1[i].rstrip("\n")+"-"+f2[i]
                temp.append(k)
            temp.extend(f1[i+1:])
            print(temp)
        elif l1<l2:
            for i in range(l1):
                k=f1[i].rstrip("\n")+"-"+f2[i]
                temp.append(k)
            temp.extend(f2[i+1:])
            print(temp)
        else:
            for i in range(l2):
                k=f1[i].rstrip("\n")+"-"+f2[i]
                temp.append(k)
            temp.extend(f1[i+1:])
            print(temp)
#________________________________________________________________________
f1=input("Enter a  filename1 :")
f2=input("Enter a  filename2 :")
import os
with open (f1,"r") as x:
    x=x.readlines()
with open(f2,"r") as y:
    y=y.readlines()
    l1=len(x)
    l2=len(y)
    z=[]
if l1>l2:
    for i in range(l2):
        k=x[i].rstrip("\n")+"-"+y[i]
        z.append(k)
    z.extend(x[i+1:])
    print(z)
elif l1<l2:
    for i in range(l1):
        k=x[i].rstrip("\n")+"-"+y[i]
        z.append(k)
    z.extend(y[i+1:])
    print(z)
else:
    for i in range(l2):
        k=x[i].rstrip("\n")+"-"+y[i]
        z.append(k)
    #z.extend(x[i+1:])# Here we wont get any extended value because its: len(x)=len(y) condition
    print(z)


#44) WAP accept 2 files and check both file contents are same or not.
import os
f1=input("Enter a File1 : ")
f2=input("Enter a File2 : ")
if os.path.exists(f1) and os.path.isfile(f1):
    if os.path.exists(f2) and os.path.isfile(f2):
        with open (f1,"r") as x:
            y=x.read()
        with open (f2,"r") as x:
            z=x.read()
            if y==z:
                print("Both file contents are same")
            else:
                print("Both file contents are not same")



#45) WAP accept a file and add  "Tecnosoft " at end of each line
import os
fn=input("Enter a File : ")
if os.path.exists(fn) and os.path.isfile(fn):
    with open (fn,"r") as x:
        y=x.readlines()
        for i in y:
            print(i.rstrip("\n")+"Tecnosoft")
