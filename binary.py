def binarysearch(a, l, r, x):
   
    if r >= l:
        mid = l + (r - l) // 2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            return binarysearch(a, l, mid-1, x)
        else:
            return binarysearch(a, mid + 1, r, x)
    else:
        return -1
       
 
a=[]
num=int(input("Enter the number of elements in the array : "))
print("Input the elements")
for n in range(num):
    elements=int(input())
    a.append(elements)
print("The array is ")
print(a)
s=len(a)-1
p=int(input("Enter the value of p - "))
x=binarysearch(a,0,s,p)
if x!=-1:
    print(p,"is found in the array at index ",x)
else:
    print("  Element not found")
   
   
    for c in range(len(a)):
        if(a[c]>p):
            print(p," can be inserted at index ",c)
            break
