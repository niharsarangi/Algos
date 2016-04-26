def partition(a,start,end):
    pivot=a[end]
    pindex=start
    for i in range(start,end):
        if a[i]<=pivot:
            a[i], a[pindex]=a[pindex],a[i]
            pindex+=1
    a[pindex],a[end]=pivot,a[pindex]
    return pindex
    
def quicksort(a,start,end):
    if start>=end:
        return
    pindex=partition(a,start,end)
    quicksort(a,start,pindex-1)
    quicksort(a,pindex+1,end)


l=[1,5,97,4,5,7,3,2,10]
quicksort(l,0,len(l)-1)
print l
