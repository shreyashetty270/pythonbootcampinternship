#1.create a function getting two input from user & print the following

def add(a,b):
    print("first number is:",a,"\nsecond number is:",b,"\n")
# adding two number:
    value = a+b
    print("addition of two numbers is :",value,"\n")
#substracting two numbers:
    value = a-b
    print("substraction of two numbers is :", value,"\n")
#dividing two numbers :
    value = a/b
    print("division of two numbers is :", value,"\n")
#multiplying two numbers:
    value = a*b
    print("multiplication of two numbers is :", value,"\n")

a=int(input("enter input 1 here:\n"))
b = int(input("enter input 2 here:\n"))
add(a,b)



#2. create following covid() & it should accept patient name,and body temperature,by default the body temperature should be 98 degree
def covid(q,w):
    print("patient name is :",q,"\tbody temperature:",w)

q = input("enter patients name:\n")
m = input("enter temperature :")
if m.isalpha() == True:
    w = 98
else:
    w = m
covid(q,w)