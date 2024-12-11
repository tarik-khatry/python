def binary_search(l,k):
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

l=[2,4,5,2,1,25,6,7,4,2,2,6,7,8]
l.sort()
print(binary_search(l,25))
