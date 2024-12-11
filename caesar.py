import string
def caesar_dictionary():
    l = string.ascii_lowercase
    l = list(l)
    d = {}
    for i in range(len(l)):
        d[l[i]] = l[(i+3)%26]
    return d

f=open('myfile.txt','r')
g=open('myfileEncp.txt','w')
d = caesar_dictionary()


c = f.read(1)
print(c)
while(c!=''):
    g.write(d[c])
    c=f.read(1)

f.close()
g.close()


