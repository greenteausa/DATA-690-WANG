z = []
i=0
for i in range(10):
    
    while True: 
        try:
            x = input("Please enter an integer:")
            y = int(x)
            break
        except:
            print("Only integer is allowed")
        
    z.append(y)    
#z=append(y)
print('Ten intergers are :',z[:])
# Minimum
def min(z):
   # i=0
    L = z[0]
    for i in range(10):
        if z[i] <= L:
            L = z[i]
        else:
            L = L
    return L

print("the min value is", min(z))

# maximum
def max(z):
   # i=0
    L = z[0]
    for i in range(len(z)):
        if z[i] >= L:
            L = z[i]
        else:
            L = L
    return L

print("the max value is ", max(z))

# range
z_range = (max(z)-min(z))
print("range is ",z_range)
#mean
def mean(z):
    #for i in range(10):
    sum=0
    for j in z:
        sum = sum + j
    mean = sum/len(z)
    return mean
print("the mean is ",mean(z))
# medium
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
z
n = len(z)
quickSort(z,0,n-1)
print ("Sorted z is:")
for i in range(n):
    print ('%d' %z[i])
def medium(z):
    i= len(z)
    if i%2 ==0:
        medium = (z[i//2-1]+z[i//2])/2
    else:
        medium = z[i//2]
    return medium   
print("the medium is ",medium(z))
#mode
H={}
H[2] = 1
H
# I use the reference link. https://www.quora.com/What-is-the-most-efficient-algorithm-for-calculating-the-mode-of-an-array-of-integers
def mode(z):
    H = {}
    maxH = 0
    mode = None
    for x in z:
        if x in H:
            H[x] =H[x] +1 
        else:
            H[x] =1
    
    value_list = list(H.values())
    maxH = max(value_list)
    mode = [k for k,v in H.items() if v == maxH]
    return mode
print("the mode is ",mode(z))
# varience
def variance(z):
    var = 0
    for i in range(len(z)):
        var += (z[i]-mean(z))**2
    return var/(len(z)-1)
print("the varience is ",variance(z))
print("the length of z is ",len(z))
# Standard Deviation
def squareRootExhaustive(x, epsilon):
  """Assumes x and epsilon are positive floats & epsilon < 1
    Returns a y such  that y*y is within epsilon of x"""
  step = epsilon ** 2
  ans = 0.0
  while abs(ans**2 - x) >= epsilon and ans*ans <= x:
    ans += step
  if ans*ans > x:
    raise ValueError
  return ans
def Standard_deviation(z):
    return squareRootExhaustive(variance(z),0.001)
print("The standard deviation is ",Standard_deviation(z))
