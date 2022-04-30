Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n=int(input("enter the n terms :"))
enter the n terms :13
n1,n2=0,1
count=0
if n<=0:
    print("please enter a positive integer ")
elif n==1:
    print("Fibonacci sequence upto",13,":")
else:
    print("Fibonacci sequence :")
    while count<n:
        print(n1)
        r=n1+n2
        n1=n2
        n2=r
        count+=1

        
Fibonacci sequence :
0
1
1
2
3
5
8
13
21
34
55
89
144
