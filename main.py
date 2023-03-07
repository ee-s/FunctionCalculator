#27/02/2023
#Function calculator

#define Function
def math(a,b):
    if start=="S":
      print (a-b)
    if start=="A":
      print (a+b)
    if start=="D":
      print (a/b)
    if start=="M":
      print (a*b)
    if start=="E":
      print(a**b)

#input
print("Hello, Wellcome to Elizas calculator")
a=input("Enter number 1 __ ")
b=input("Enter number 2 __ ")
start=input("Brilliant pick a function multi(M) divide(D) add(A) substract(S) Exponent(E) "). upper()
#output
print(math(int(a),int(b)))
