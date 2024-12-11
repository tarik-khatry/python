'''def binary_search(l,k):
    begin=0
    end=len(l)-1
    while(end-begin>1):
        mid=(begin+end)//2
        if(l[mid]<k):
            begin=mid+1
        if(l[mid]>k):
            end=mid-1
        if(l[mid]==k):
            return 1
    if (l[begin]==k) or (l[end]==k):
        return 1
    else:
        return 0

l=list(range(1000))
l.sort()
print(binary_search(l,998))'''

#Using Recursion
def recursive_binary_search(l,k,begin,end):
    if(begin==end):
        if (l[begin]==k):
            return 1
        else:
            return 0
    if (end-begin==1):
        if (l[begin]==k) or (l[end]==k):
            return 1
    if (end-begin<0):
        return 0
    if (end-begin>1):
        mid=(begin+end)//2
        if (l[mid]>k):
            end=mid-1
        if (l[mid]<k):
            begin=mid+1
        if (l[mid]==k):
            return 1
    return recursive_binary_search(l,k,begin,end)

l=list(range(1000))
print(recursive_binary_search(l,235,0,len(l)-1))