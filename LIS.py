list1 = [1,1,2,4,3,5,7,5,4,6,7,7,8,9]
l = len(list1)
seqlist = []
longlist = []

if l > 0:
    seqlist = [list1[0]]

for i in range(0,l):
    s1 = list1[i]
    if i > 0:
        if s1>= list1[i-1]:
            seqlist.append(s1)
        else:
            if len(seqlist) > len(longlist):
                longlist = seqlist.copy()
            seqlist.clear()
            seqlist = [list1[i]]
        
if len(seqlist) > len(longlist):
    longlist = seqlist.copy()
elif len(longlist) == 0:
    longlist = list1.copy()
print(longlist)
   
