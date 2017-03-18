def BinarySearch(l,key):
    low = 0
    high=len(l)-1
    i=0
    while(low<=high):
        i=i+1
        mid=(low+high)//2
        if(l[mid]>key):
            high=mid
        elif(l[mid]<key):
            low=mid
        else:
            print ('use %d times' %i)
            return mid+1
    return -1
if __name__=='__main__':
    l=[1,5,6,9,10,51,62,65,70]
    print(BinarySearch(l,10))
    print(BinarySearch(l,9))
    print(BinarySearch(l,51))
    print(BinarySearch(l,6))
