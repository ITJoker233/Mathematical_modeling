
def sort(raw_data):
    return list(set(raw_data))

def quickSort(arr):    
    if len(arr) <= 1:        
        return arr    
    pivot = arr[len(arr) // 2]    
    left = [x for x in arr if x < pivot]    
    middle = [x for x in arr if x == pivot]    
    right = [x for x in arr if x > pivot]    
    return quickSort(left) + middle + quickSort(right)

def readFile(path,mode='r+'):
    with open(path,mode) as f:
        data = f.read()
    return data

def writeFile(path,data,mode='w+'):
    with open(path,mode) as f:
        f.write(data)