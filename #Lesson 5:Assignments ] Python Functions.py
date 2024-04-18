#Lesson 5:Assignments ] Python Functions
#1.The Calculator App
#Task 1: Create function
#Find the sum
print("Find the Sum")
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter an integer: "))
num3 = num1 +num2
print("The sum of the numbers is:", num3)
#Find the diference
print("Find the diference")
dif1 = int(input("Enter an integer: "))
dif2 = int(input("Enter an integer: "))
dif3 = dif1 - dif2
print("The diference of the numbers is:", dif3)
#Multiplication
print("Find the Multiplication")
Mult1 = int(input("Enter an integer: "))
Mult2 = int(input("Enter an integer: "))
Mult3 = Mult1 * Mult2
print("The product of the numbers is:", Mult3)
#Division
print("Find the Quotient")
Div1 = int(input("Enter an integer: "))
Div2 = int(input("Enter an integer: "))
if Div2 == 0:
    Div3 = print("Cannot divide by zero")
else:
    Div3 = Div1 / Div2
print("The quotient of the numbers is:", Div3)
#Task 2:Operations Choice
d1a = input ("Do you want to find the sum diference multiply or divide? ")
if d1a == "sum":
        num1 = int(input("Enter an integer: "))
        num2 = int(input("Enter an integer: "))
        num3 = num1 + num2
        print("The quotient of the numbers is:", num3)
elif d1a == "diference":
        dif1 = int(input("Enter an integer: "))
        dif2 = int(input("Enter an integer: "))
        dif3 = dif1 - dif2
        print("The quotient of the numbers is:", dif3)
elif d1a == "multiply":
        Mult1 = int(input("Enter an integer: "))
        Mult2 = int(input("Enter an integer: "))
        Mult3 = Mult1 * Mult2
        print("The quotient of the numbers is:", Mult3)
elif d1a == "divide":
     print("Find the Quotient")
Div1 = int(input("Enter an integer: "))
Div2 = int(input("Enter an integer: "))
if Div2 == 0:
    print("Cannot divide by zero")
else:
    Div3 = Div1 / Div2
    print("the quotient is",Div3)
#2. The Shopping List Maker
#Task 1
# use a fuction we can call in it use while loop to ask what we want to add to get users input their input add to my list by apend is the best way to add
#add it to back of the list let them continue to add things
Shoping_list = ['Ice cream', 'jello', 'gummies', 'life savers']
print(Shoping_list)
print("lets go shopping")
action=input("go, remove, stop or add")
if action == "go":
    print("Shoping is a go")
elif action == "add":    
    print("add an item to the shoping list")
    Shoping_list.append(input("Enter an item"))
    print(Shoping_list)
elif action == "remove": 
        print("remove an item from the shoping list")
        Shoping_list.remove(input("Enter an item to remove"))
        print(Shoping_list)
elif action == "stop":
     print(Shoping_list)
else: 
     print("Shoping Complete")
#Remove an item from the list
#3
#Task 1 
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
def Average(grades):
    return sum(grades)/ len(grades)
print("Average of the grades =")
print(Average(grades))
#Task 2 

def low(grades):
    return min(grades)
print("Lowest grade =")
print(min(grades))
