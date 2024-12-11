#recursion lessons iitm

def compound(p,y):
    if (y==1):
        return p*1.1
    else:
        return compound(p,y-1)*1.1 
print(compound(1000,50))       