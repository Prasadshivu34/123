def bubblesort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
x=[23,56,87,98,67]
print("before sorting:",x)
bubblesort(x)
print("after sorting:",x)
                
                
                      
                

