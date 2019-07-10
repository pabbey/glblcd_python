list = []
list.append('a')
print (list)



      
      
def viv(min,max):
    for h in range(min,max):
        if(h%2==0):
            list = [min,max]
            list.append(h)
    return list

value = viv(2,8)
print(value)
value = viv(10,20)
print(value)
value = viv(20,30)
print(value)
      
      
    

            
    
    