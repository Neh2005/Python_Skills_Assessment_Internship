#Program to print the pattern

def num(n):
  for i in range (1,n+1):
    for j in range (i):
      print("*", end=" ")
    print(" ")
num(10)


#Program to print the table if any number till 10 rows

def num(n):
  
  for i in range(1,11):
      print(i,"*",n,"=",end="\t")
      print(i*n, end="\t")
      print()
num(12)


#Program to accept any number and print the student name with that id

def dict():
    d1={'id':1,'name':"rajesh"},{'id':2,'name':"rahul"},{'id':3,'name':"sruthi"}
    list=[d1]
    n=int(input("Enter the id of the student"))
    return(d1[n-1])
print(dict())



