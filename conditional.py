#i = 8
#if(i % 2 == 0):
#    print ("Even Number")
#else:
#    print ("Odd Number")
    
    
def evens(numbers):
    ans=0
    for d in numbers:
        if(d%2==0):
            ans = ans+d
    return ans   
            
print(evens([2,9,5,3,1,8]))






def P_age():
    a = int (input("how old are you "))
    if( a > 40):
        return(a ,"yeasr" ,"you are old")
    elif( a < 40):
        return(a ,"year" ,"you are still young")
    else:
        return ("invalid input")
print(P_age())  
        