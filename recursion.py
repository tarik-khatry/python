#recursion lessons iitm

'''def compound(p,y):
    if (y==1):
        return p*1.1
    else:
        return compound(p,y-1)*1.1 
print(compound(1000,50))       '''

#check 0  in a list
l=[3,2,5,6,2,3,5,6,0,5,53,6]
def check0(n):
    if (n[0]==0):
        return 1    
    else: 
        return check0(n[1:])
print(check0(l))