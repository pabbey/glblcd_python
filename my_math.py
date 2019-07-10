def calculate():
    a=input("what operation do want to perform ? ")
    if a =="ADD" or "add":
        b=input("enter the fisrt number ")
        c=input("enter the second numbe ")
        print(b + c)
    elif a == "SUBSTRACT" or "substract":
        b=input("enter the fisrt number ")
        c=input("enter the second numbe ")
        print(b - c)
    
    elif a == "MULTIPLY" or "multiply":
        b=input("enter the fisrt number ")
        c=input("enter the second numbe ")
        print(b * c)
    elif a == "DIVIDE" or "divide":
        b=input("enter the fisrt number ")
        c=input("enter the second numbe ")
        print(b / c)
    else:
        print("invalid!!!!! type operation in uppercae or lowercase:")
    
print(calculate())
        
        
    