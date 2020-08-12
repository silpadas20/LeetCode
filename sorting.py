def bubble(arr):
    for i in range(len(arr)-1):
        j=0
        while j < len(arr)-1:
            if arr[j] > arr[j+1]:
                temp= arr[j]
                arr[j]= arr[j+1]
                arr[j+1]= temp
            j+=1
    return arr
    
b=bubble([1,5,3,7,32,68,2])
print(b)

def selection(arr):
    for i in range(len(arr)-1):
        min_el=min(arr[i:])
        temp=arr[i]
        arr[arr.index(min_el)]=temp
        arr[i]=min_el

    return arr
s=selection([2,5,3,7,32,68,1])
print(s)

def insertion(arr):
    for i in range(len(arr)-1):
        sort = arr[:i+1]
        for j in range(len(sort),0,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
    
    return arr
ins=insertion([2,5,3,7,32,68,1])
print(ins)

def merge_sort(arr):
    
    if len(arr)>1:
        mid = len(arr)/2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1
			
	return arr		
			
			
def quick(arr):
    pivot=arr[0]
    i,j,k=1,-1,0
    found=False
    while not found:
        if arr[i] > pivot:
            i+=1
        if arr[j] < pivot:
            j=j-1
        arr[i],arr[j]=arr[j],arr[i]
        
        if arr[i] > arr[j]:
            found=True
            arr[0],arr[j]=arr[j],arr[0]
            quick(arr[:j])
            quick(arr[j:])    
    return arr
arr=[2,34,5,67,8,21,3,54,6]
q=quick(arr)
print(q)

#shell sort
def shell(arr):
    loop=(len(arr)//2)-1
    
    while loop < len(arr) and loop >= 0: 
        differ = 3*loop+1
        first_dif= 0
        next_dif = differ + first_dif
            
        while next_dif < len(arr):
            print(first_dif,next_dif)
            if arr[first_dif] > arr [next_dif] :
                temp=arr[first_dif]
                arr[first_dif]= arr[next_dif]
                arr[next_dif]= temp
                    
            first_dif += 1
            next_dif= differ + first_dif

        loop-=1

    return arr
print(shell([3,9,5,2,1,7,44,6]))

----  proper solution -----
def shell_sort(arr):
    sublistcount = len(arr)/2
    
    # While we still have sub lists
    while sublistcount > 0:
        for start in range(sublistcount):
            # Use a gap insertion
            gap_insertion_sort(arr,start,sublistcount)

      

        sublistcount = sublistcount / 2

def gap_insertion_sort(arr,start,gap):
    for i in range(start+gap,len(arr),gap):

        currentvalue = arr[i]
        position = i

        # Using the Gap
        while position>=gap and arr[position-gap]>currentvalue:
            arr[position]=arr[position-gap]
            position = position-gap
        
        # Set current value
        arr[position]=currentvalue

## Quick sort ##
def quick(arr):
    pivot = arr[0]
    
    i,j = 1, len(arr)-1
    while i <= j :
        for i in range(1,len(arr)):
            if arr[i] >= pivot :
                pos_i = i
                break
                
        for j in range(len(arr)-1,0,-1):
            if arr[j] < pivot :
                pos_j = j
                break
        
        if arr[pos_i] > arr[pos_j]:
            arr[pos_i],arr[pos_j]= arr[pos_j],arr[pos_i]
        
    if arr[0] > arr[j] :
        arr[0] = arr[j]
        arr[j] = pivot

    quick(arr[:j])
    quick(arr[j+1:])

quick([1,3,5,7,9,2,6,0,1])

        
## pascal
n= int(input('enter the number of rows: '))
list1=[]
for i in range(n):
    temp_list=[]
    for j in range(i+1):
        if j==0 or j==i:
            temp_list.append(1)
        else:
            temp_list.append(list1[i-1][j-1]+list1[i-1][j])
    list1.append(temp_list)

print(list1)
for i in range(n):
    for j in range(n-i-1):
        print(" ",end= "")
    for j in range(i+1):
        print(list1[i][j],end= " ")#list1[i][j]=list1[i-1][j-1]+list1[i-1][j]
    print()
        
        
       