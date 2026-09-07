try : 
    a=int(input("enter first number : "))
    b=int(input("enter second number : "))

    print("enter the operation which you want to perform on these two numbers : like if you want to add press '+', if you want to subtract press '-', if you want to multiply press '*', if you want to divide press '/', if you want to get a rounded off value after division press '//', if you want remainder after division press '%' : ")
    op=input("enter an operator (+,-,*,/,//,%) : ")

    match op:
        case '+' :
            print(f"sum of {a} and {b} is {a+b}")
        case '-' :
            print(f"difference of {a} and {b} is {a-b}")
        case '*' :
            print(f"product of {a} and {b} is {a*b}")
        case '/' :
            print(f"quoitent of {a} divided by {b} is {a/b}")
        case '%' :
            print(f"remainder of {a} divided by {b} is {a%b}")
        case '//' :
            print(f"rounded off quoitent of {a} divided by {b} is {a//b}")
        case default :
            print("enetr a valid operator ")
except Exception as e :
    print("enter valid numbers ")

